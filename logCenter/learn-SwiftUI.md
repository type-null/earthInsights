# Developing Applications for iOS using SwiftUI

Stanford University, CS193p, Spring 2020

Course Website: https://cs193p.sites.stanford.edu

## Table of Contents
1. [**Course Logistics and Intro to SwiftUI**](#1)
    > After going over the mechanics of how the course works, this first lecture dives right into creating an iOS application (a card-matching game called Memorize).  The Xcode development environment is used to demonstrate the basics of SwiftUI's declarative approach to composing user-interfaces.
    > [Video](https://youtu.be/jbtqIBpUG7g), [Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/l1.pdf)

2. [**MVVM and the Swift Type System**](#2)
    > Conceptual overview of the architectural paradigm underlying the development of applications for iOS using SwiftUI: MVVM.  In addition, a key underpinning of the Swift Programming Language, its type system, is explained.  The Memorize demonstration continues, incorporating MVVM.
    > [Video](https://youtu.be/4GjXq2Sr55Q),
[Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/l2.pdf),
[Reading 1](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/r1.pdf),
[Assignment 1](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/a1.pdf)
    
3. [**Reactive UI Protocols Layout**](#3)
    > Now that MVVM has been applied to Memorize, we can use the reactive nature of SwiftUI to make the cards flip over by processing multitouch events, updating our Model through our ViewModel and having our UI stay in sync with our Model at all times.  An important concept, protocols, is covered in more detail as well as the basics about how to lay out Views in the UI.
    > [Video](https://www.youtube.com/watch?v=SIYdYpPXil4&list=PLpGHT1n4-mAtTj9oywMWoBx0dCGd51_yG&index=3),
[Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/l3.pdf)

4. [**Grid enum Optionals**](#4)
    > The survey of the Swift type system completes with a discussion of enum.  An important language construct, Optionals, is both explained in slides and then demonstrated in Memorize as we fully implement the logic of the game.
    > [Video](https://www.youtube.com/watch?v=eHEeWzFP6O4&list=PLpGHT1n4-mAtTj9oywMWoBx0dCGd51_yG&index=4),
[Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/l4.pdf),
[GridLayout.swift](https://cs193p.stanford.edu/Spring2020/GridLayout.swift.zip),
[Reading 2](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/r2_0.pdf),
[Assignment 2](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/a2_0.pdf)

5. [**ViewBuilder Shape ViewModifier**](#5)
    > Access Control.  More about drawing, including the @ViewBuilder construct for expressing a conditional list of Views, the Shape protocol for custom drawing and ViewModifier, a mechanism for making incremental modifications to Views.
    > [Video](https://www.youtube.com/watch?v=oDKDGCRdSHc),
[Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/lecture_5.pdf)

6. [**Animation**](#6)
    > @State (temporary state in a View) and property observers.  Deep dive into animation, including implicit vs. explicit animations, transitions, Shape animations, animating ViewModifiers and more.  Animate flipping of cards, new game and “pie” bonus countdown.
    > [Video](https://www.youtube.com/watch?v=3krC2c56ceQ),
[Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/lecture_6.pdf),
[Reading 3](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/reading_3.pdf),
[Assignment 3](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/assignment_3.pdf)
    
    






<a name="1"></a>
# Lecture 1: Course Logistics and Intro to SwiftUI

[Video](https://youtu.be/jbtqIBpUG7g),
[Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/l1.pdf)

<a name="2"></a>
# Lecture 2: MVVM and the Swift Type System
[Video](https://youtu.be/4GjXq2Sr55Q),
[Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/l2.pdf),
[Reading 1](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/r1.pdf),
[Assignment 1](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/a1.pdf)

## MVVM
<img src="https://i.imgur.com/vNMol5j.png" width=800 alt="MVVM"/>

## Varieties of Types

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
  
  
  
## Reading 1 notes
### Arrays
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

### Dictionaries
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

### For-in loops
- `stride(from:to:by:)`, closed range: `stride(from:through:by:)`
  ```swift
  let minuteInterval = 5
  for tickMark in stride(from: 0, to: minutes, by: minuteInterval) {
      // render the tick mark every 5 minutes (0, 5, 10, 15 ... 45, 50, 55)
  }
  ```
### Switch
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

### Early exit
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

### Closure
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

### Type Properties
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

### Methods
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
  - `class` stores in heap and has pointers so always can change.
  - `init` can change property without keyword `mutating`.
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
  


<a name="3"></a>
# Lecture 3 Reactive UI Protocols Layout

[Video](https://www.youtube.com/watch?v=SIYdYpPXil4&list=PLpGHT1n4-mAtTj9oywMWoBx0dCGd51_yG&index=3),
[Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/l3.pdf)


- **ViewModel**: Property wrapper `@Published` *calls* `objectWillChange.send()` everytime `gameModel` changes
  ```swift
  @Published private var gameModel: MemoryGame<String> = EmojiMemoryGame.createMemoryGame()
  ```
- **View**: Property wrapper `@ObservedObject` *redraws* everytime the `ObservableObject` says `objectWillChange.send()`
  ```swift
  @ObservedObject var gameViewModel: EmojiMemoryGame
  ```
  
## Protocols
- A protocol is a type.
- Sort of "stripped-down" struct/class: has funcs and vars, but no implementation (or storage)!
  ```swift
  protocol Moveable {
      func move(by: Int)
      var hasMoved: Bool { get } // read only
      var distanceFromStart: Int { get set } // read/write
  }
  ```
  
- Now, any other type can *claim to implement* `Moveable`
  ```swift
  struct PortableThing: Moveable {
      // must implement move(by:), hasMoved and distanceFromStart here
  }
  ```

- "Protocol inheritance":
  ```swift
  protocol Vehicle: Moveable {
      var passengerCount: Int { get set }
  }
  class Car: Vehicle {
      // must implement move(by:), hasMoved, distanceFromStart and passengerCount here
  }
  ```

- Claim to implement multiple protocols:
  ```swift
  class Car: Vehicle, Impoundable, Leasable {
      // must implement move(by:), hasMoved, distanceFromStart and passengerCount here
      // and must implement any funcs/vars in Impoundable and Leasable too
  }
  ```

### Protocol Extension
Adding protocol implementation
- "Constrains and gains"

- `extentsion`

- Generics and protocols
```swift
extension Array where Element: Greatness {
    var greatest: Element {
        // for-loop through all the Elements
        // which (inside this extension) we know each implements the Greatness protocol // and figure out which one is greatest by calling isGreaterThan(other:) on them
        return the greatest by calling isGreaterThan on each Element
    }
}
```
`Greatness` is a protocol. This part `where` means we don't care about `Array` unless it is an `Array` of `Greatness`.

- add “default implementations” of the protocol’s own funcs/vars

### Extension
- You can use an extension to add things to structs and classes too.

- You can even make something conform to a protocol purely via an extension ...

### Generics and Protocols


## Layout

3 steps:
  1. Container Views “offer” space to the Views inside them
  2. Views then choose what size they want to be
  3. Container Views then position the Views inside of them

### Container Views
- The “stacks” (`HStack`, `VStack`) divide up the space offered to them amongst their subviews 
- `ForEach` defers to its container to lay out the Views inside of it
- Modifiers (e.g. `.padding()`) essentially “contain” (return) the View they modify. Some do layout.

#### HStack and VStack
It offers space to its “least flexible” (with respect to sizing) subviews first. (Image > Text > Shape)

- Commonly put in stacks:
  ```swift
  Spacer(minLength: CGFloat)
  // Always takes all the space offered to it.
  // Draws nothing.
  // The minLength defaults to the most likely spacing you’d want on a given platform.
  
  Divider()
  // Draws a dividing line cross-wise to the way the stack is laying out.
  // For example, in an HStack, Divider draws a vertical line.
  // Takes the minimum space needed to fit the line in the direction the stack is going.
  
  ```
- `.layoutPriority(Double)`

- argument: `alignment: .leading`

#### Modifiers

#### GeometryReader
You wrap this `GeometryReader` View around what would normally appear in your View’s body
```swift
var body: View {
    GeometryReader { geometry in // not showing content: parameter label
        ...
    }
}

// The geometry parameter is a GeometryProxy. 
struct GeometryProxy {
    var size: CGSize
    func frame(in: CoordinateSpace) -> CGRect
    var safeAreaInsets: EdgeInsets
}
```
- `GeometryReader` itself (it’s just a View) *always accepts all the space offered to it*.

#### Safe Area
- To ignore safe area:
  ```swift
  ZStack { ... }.edgesIgnoringSafeArea([.top]) // draw in “safe area” on top edge
  ```
  
#### How exactly do containers "offer" space to Views they contain?

- With the modifier `.frame(...)`
- `.position(CGPoint)`
- `.offset(CGSize)`



<a name="4"></a>
# Lecture 4 Grid enum Optionals

[Video](https://www.youtube.com/watch?v=eHEeWzFP6O4&list=PLpGHT1n4-mAtTj9oywMWoBx0dCGd51_yG&index=4),
[Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/l4.pdf),
[GridLayout.swift](https://cs193p.stanford.edu/Spring2020/GridLayout.swift.zip),
[Reading 2](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/r2_0.pdf),
[Assignment 2](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/a2_0.pdf)

- `@escaping` for functions used in later functions

- Name files contain `extension`s like "Array+Identifiable.swift"


## enum
An enum is a *value type* (like struct), so it is copied as it is passed around
- It does not live in the heap, no pointers to it (class does).

- Use `CaseIterable` and `allCases` to get whole collection of an enum and iterate.
  ```swift
  enum Beverage: CaseIterable {
    case coffee, tea, juice
  }
  let numberOfChoices = Beverage.allCases.count
  ```

### Associated value
- Implicitly Assigned Raw Values
  - Use `Int` to store integer values of enumeration
    ```swift
    enum Planet: Int {
      case mercury = 1, venus, earth, mars, jupiter, saturn, uranus, neptune
    }
    ```
  - `String`
  ```swift
  enum CompassPoint: String {
    case north, south, east, west
  }
  ```
  - Access raw value:
  ```swift
  let earthsOrder = Planet.earth.rawValue
  // earthsOrder is 3

  let sunsetDirection = CompassPoint.west.rawValue
  // sunsetDirection is "west"
  ```

- Recursive Enumerations
  - Add `indirect` before `case` or `enum`

### Optionals
- Access associated value either by 
  - Force unwrapping with `!`
  - or safely using `if let`
    - use `,` as sequencial AND instead of `&&`
      ```swift
      if let chosenIndex: Int = cards.firstIndex(matching: card), !cards[chosenIndex].isFaceUp {
        ...
      }
      ```
  
- "Optional defaulting" `??` (nil coalescing operator)
  ```swift
  let x: String? = ...
  let y = x ?? "foo"
  ```

## Reading 2

### Closure

- Escaping Closures
  - One way that a closure can escape is by being stored in a variable that is defined outside the function. 
  - Marking a closure with @escaping means you have to refer to self explicitly within the closure.
  ```swift 
  struct Grid<Item, ItemView>: View where Item: Identifiable, ItemView: View {
    var items: [Item]
    var viewForItem: (Item) -> ItemView
    
    init(_ items: [Item], viewForItem: @escaping (Item) -> ItemView) {
        self.items = items
        self.viewForItem = viewForItem
    }
  }
  ```


- Autoclosures
  - delays evaluation (because it's a function)

### Enum




<a name="5"></a>
# Lecture 5 ViewBuilder Shape ViewModifier

[Video](https://www.youtube.com/watch?v=oDKDGCRdSHc),
[Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/lecture_5.pdf)









<a name="6"></a>
# Lecture 6 Animation

[Video](https://www.youtube.com/watch?v=3krC2c56ceQ),
[Slides](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/lecture_6.pdf),
[Reading 3](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/reading_3.pdf),
[Assignment 3](https://cs193p.sites.stanford.edu/sites/g/files/sbiybj16636/files/media/file/assignment_3.pdf)

## Property Observers

“Watching” a var and reacting to changes

- `willSet` -> `newValue`, `didSet` -> `oldValue`

- completely unrelated to computed var

## @State

State that is entirely localized inside a `View`

Only used for *temporary* state like presentations of alerts or editing things or animation

- You must mark any vars used for this temporary state with `@State` ...
  ```swift
    @State private var somethingTemporary: SomeType // this can be of any type
  ```
  
  Marked private because no one else can access this anyway (except upon creating your View). Changes to this `@State` var _will cause your View to redraw if necessary_!
In that sense, it’s just like an `@ObservedObject`.

## Animation

You can only animate **changes** to Views in containers that are already on screen (CTAAOS).
  - The appearance and disappearance of `Views` in CTAAOS.
  - Changes to the arguments to `Animatable` view modifiers of `Views` that are in CTAAOS.
  - Changes to the arguments to the creation of `Shapes` inside CTAAOS.
  
To make an animation "go":
  - Implicitly, by using the view modifier `.animation(Animation)`.
  - Explicitly, by wrapping `withAnimation(Animation) { }` around code that might change things.

### Implicit vs. Explicit Animation

#### Implicit Animation

- “Automatic animation”
-  add a `.animation(Animation)` view modifier to the `View` you want to auto-animate.
  ```swift
  Text(“👻 ”)
      .opacity(scary ? 1 : 0)
      .rotationEffect(Angle.degrees(upsideDown ? 180 : 0)) 
      .animation(Animation.easeInOut) // Swift could infer the Animation. part, of course
  ```
- **Warning!** The `.animation` modifier does not work how you might think on a container. A container just _propagates_ the `.animation` modifier to all the Views it contains.

In other words, `.animation` does not work not like `.padding`, it works more like `.font`.

- The argument to .animation() is an Animation struct.
It lets you control things about an animation ...

1. duration
  - delay
  - repeat or even `repeatForever`
  
2. curve
  - controls the rate at which the animation “plays out” (it’s “curve”) ...
  - `.linear`
  - `.easeInOut`: sigmoid
  - `.spring`: "soft landing" "bounce"
  
- Implicit are mostly used on “leaf” (i.e. non-container) Views. on Views that are typically working independently of other Views.

Recall that you can’t implicitly animate a container view (it propagates to the Views inside). That’s because in containers you start wanting to be able to coordinate the Views’ animations. Essentially, a bunch of Views that are contained together want to animate together.
And they likely will all animate together in response to some user action or Model change. That’s where explicit animation comes in ...

#### Explicit

- appear in closures like `.onTapGesture`

- You supply the Animation (duration, curve, etc.) to use and the block of code. 

  ```swift
  withAnimation(.linear(duration: 2)) {
      // do something that will cause ViewModifier/Shape arguments to change somewhere 
  }
  ```
- **Explicit animations do not override an implicit animation.**

### Animating Views

(via their ViewModifiers which can implement the Animatable protocol)


### Transitions

(animating the appearance/disappearance of Views by specifying ViewModifiers)

- A transition is nothing more than a _pair_ of `ViewModifiers`:
  - “before”, "after"


### Animating Shapes

(via the `Animatable` protocol)

## Internationalize string
`LocalizedStringKey`
