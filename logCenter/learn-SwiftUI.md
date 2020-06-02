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

- "Don't Care" type (aka generics)

- `enum`

- functions
