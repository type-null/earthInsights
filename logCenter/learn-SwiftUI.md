# Developing Applications for iOS using SwiftUI

Stanford University, CS193p, Spring 2020

Course Website: https://cs193p.sites.stanford.edu

## Lecture 1: Course Logistics and Intro to SwiftUI

[Video](https://youtu.be/jbtqIBpUG7g),
[Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/l1.pdf)

## Lecture 2: MVVM and the Swift Type System
[Video](https://youtu.be/4GjXq2Sr55Q),
[Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/l2.pdf),
[Reading 1](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/r1.pdf),
[Assignment 1](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/a1.pdf)

### MVVM
<img src="https://i.imgur.com/vNMol5j.png" width=800 alt="MVVM"/>

### Varieties of Types

- `struct` and `class`
  
  Both have pretty much exactly the same syntax.
  
  Whenever you define a new structure or class, you define a new Swift type. Give types `UpperCamelCase` names. (Give properties and methods `lowerCamelCase` names)
  
  - stored `var`s (the kind you are used to, i.e., stored in memory)
    ```swift
    var isFaceUp: Bool
    ```
  - computed `var`s (i.e. those whose value is the result of evaluating some code)
    ```swift
    var body: some View {
        return Text(“Hello World”)
    }
    ```
  
  - constant `let`s (i.e. `var`s whose values never change)
    ```swift
    let defaultColor = Color.orange
    ...
    CardView().foregroundColor(defaultColor)
    ```
  
  - `func`tions
    ```swift
    func multiply(operand: Int, by: Int) -> Int {
        return operand * by
    }
    multiply(operand: 5, by: 6)

    // can have two labels for each parameter: external-name, internal-name
    func multiply(_ operand: Int, by otherOperand: Int) -> Int { 
        return operand * otherOperand
    }
    multiply(5, by: 6)
    ```
    
  - `init`ializers (i.e. special functions that are called when creating a `struct` or `class`)
    ```swift
    struct MemoryGame {
        init(numberOfPairsOfCards: Int) {
            // create a game with that many pairs of cards
        }
    }
    ```
  
  So what’s the difference between struct and class?
  
  <img src="https://i.imgur.com/EA7mbVT.png" width=600 alt="struc vs class">
  
  Class is easy to share: lives in heap and has pointers to it.
  
- `protocol`

- "Don't Care" type (aka generics, type parameter)
  
  But Swift is a strongly-typed language, so we don’t use variables and such that are “untyped.”
  
  Awesome example of generics: `Array`. It doesn’t care at all what type it contains.
    ```swift
    struct Array<Element> {
      ...
      func append(_ element: Element) { . . . }
    }
    ```
    The type of the argument to append is `Element`. A “don’t care” type.
    
    Element is not any known struct or class or protocol, it’s just a placeholder for a type.
    
    The code for using an Array looks something like this ...
    ```swift
    var a = Array<Int>()
    a.append(5)
    a.append(22)
    ```
    When someone *uses* Array, *that’s* when Element gets determined (by `Array<Int>`).

  
  

- `enum`

- functions as types
  
  Examples ...
  ```swift
  (Int,Int)->Bool //takestwoIntsandreturnsaBool
  (Double) -> Void // takes a Double and returns nothing
  () -> Array<String> // takes no arguments and returns an Array of Strings
  () -> Void // takes no arguments and returns nothing (this is a common one)
  ```
  All of the above a just types. No different than Bool or View or Array<Int>. All are types. 
  
  So we can create vars whose type are functions:
  
  ```swift
  var foo: (Double) -> Void // foo’s type: “function that takes a Double, returns nothing”
  func doSomething(what: () -> Bool) // what’s type: “function, takes nothing, returns Bool”
  ```
  
  ```swift
  var operation: (Double) -> Double
  
  func square(operand: Double) -> Double {
      return operand * operand
  }
  
  operation = square // just assigning a value to the operation var, nothing more
  let result1 = operation(4) // result1 would equal 16
  // Note that we don’t use argument labels (e.g. operand:) when executing function types.
  ```
  + CLosure
    
    We call such an inlined function a “closure” and there’s special language support for it.
    
    Remember that we are mostly doing “**functional** programming” in SwiftUI.
    As the very name implies, “functions as types” is a very important concept in Swift. Very.
  
  
  
### Reading 1 notes
#### Arrays
- repeating array: `var board = [Int](repeating: 0, count: 10)`
- Some methods: `.count`, `.isEmpty`, 
- `.append("Flour")` == `+= ["Flour"]`
```swift
var firstItem = shoppingList[0]
// to change a range of values
shoppingList[4...6] = ["Bananas", "Apples"]
shoppingList.insert("Maple Syrup", at: 0)
// remove also returns removed item
let mapleSyrup = shoppingList.remove(at: 0)
let apples = shoppingList.removeLast()
```
- `.enumerated()` -> (index, value)
- The largest valid index in an array is `count` - 1 because arrays are indexed from zero—however, when `count` is 0 (meaning the array is empty), there are no valid indexes.

#### Dictionaries
- initializer `[Int: String]()`, set to empty dict `[:]`
- Some methods: `.count`, `.isEmpty`, 
- subscript syntax `airports["LHR"] = "London"`, but to return _oldValue_ was replaced:
  ```swift
  // returns an optional value
  if let oldValue = airports.updateValue("Dublin Airport", forKey: "DUB") {
    print("The old value for DUB was \(oldValue).")
  }
  ```
- to remove: `airports["APL"] = nil` or `airports.removeValue(forKey: "APL")` (-> removedValue)
- `.keys`, `.values`

#### For-in loops
- `stride(from:to:by:)`, closed range: `stride(from:through:by:)`
  ```swift
  let minuteInterval = 5
  for tickMark in stride(from: 0, to: minutes, by: minuteInterval) {
      // render the tick mark every 5 minutes (0, 5, 10, 15 ... 45, 50, 55)
  }
  ```
#### Switch
```swift
// Interval Matching
case 1..<5:
// Tuples
case (0, _):
    print("\(somePoint) is on the y-axis")
case (-2...2, -2...2):
    print("\(somePoint) is inside the box")
// Value Bindings
case (let x, 0):
    print("on the x-axis with an x value of \(x)")
// Where (check for additional conditions)
case let (x, y) where x == y:
    print("(\(x), \(y)) is on the line x == y")
// Compound Cases
case (let distance, 0), (0, let distance):
    print("On an axis, \(distance) from the origin")
// must be exhaustive
default:
    print("Not on an axis")
```

#### Early exit
`guard`
- like an `if` statement, executes statements depending on the Boolean value of an expression
- but always has an `else` clause
```swift
func greet(person: [String: String]) {
    guard let name = person["name"] else {
        return
    }

    print("Hello \(name)!")

    guard let location = person["location"] else {
        print("I hope the weather is nice near you.")
        return
    }

    print("I hope the weather is nice in \(location).")
}

greet(person: ["name": "John"])
// Prints "Hello John!"
// Prints "I hope the weather is nice near you."
greet(person: ["name": "Jane", "location": "Cupertino"])
// Prints "Hello Jane!"
// Prints "I hope the weather is nice in Cupertino."
```

#### Closure
- syntax:

{ (_parameters_) -> _return type_ `in`
    _statements_
}
```swift
reversedNames = names.sorted(by: { (s1: String, s2: String) -> Bool in return s1 > s2 } )
// Inferring Type From Context, Single statement can omit return
reversedNames = names.sorted(by: { s1, s2 in s1 > s2 } )
// Shorthand Argument Names
reversedNames = names.sorted(by: { $0 > $1 } )
// Operator Methods
reversedNames = names.sorted(by: >)
```
- Trailing CLosures: pass a closure expression to a function as the function’s **final** argument
```swift
reversedNames = names.sorted() { $0 > $1 }
// If a closure is only argument, () can be omitted
eversedNames = names.sorted { $0 > $1 }
```

#### Type Properties
- Properties that belong to the type itself, not to any one copy instance of that type.
- Unlike stored instance properties, you must always give stored type properties a default value.
- `static` for `struct`, `enum`, `class`
- Use `class` to allow subclasses to override the superclass’s implementation.
```swift
class SomeClass {
    static var storedTypeProperty = "Some value."
    static var computedTypeProperty: Int {
        return 27
    }
    class var overrideableComputedTypeProperty: Int {
        return 107
    }
}
```

#### Methods
- You use the `self` property to refer to the current instance within its own instance methods.
  ```swift
  struct Point {
      var x = 0.0, y = 0.0
      func isToTheRightOf(x: Double) -> Bool {
          return self.x > x
      }
  }
  ```
  
- `mutating func`: the properties of a value type (`struct`, `enum`) cannot be modified from within its instance methods _unless_ use `mutating` behavior for the modifying method.
  ```swift
  struct Point {
    var x = 0.0, y = 0.0
    mutating func moveBy(x deltaX: Double, y deltaY: Double) {
        x += deltaX
        y += deltaY
    }
  }
  var somePoint = Point(x: 1.0, y: 1.0)
  somePoint.moveBy(x: 2.0, y: 3.0)
  print("The point is now at (\(somePoint.x), \(somePoint.y))")
  // Prints "The point is now at (3.0, 4.0)"
  ```
  
- **Type Methods**: `static func`, methods that are called on the type itself than an instance of that type. `class` to override superclass. 
  




