# CS193p Developing Applications for iOS using SwiftUI

Stanford University

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
  
  
  
