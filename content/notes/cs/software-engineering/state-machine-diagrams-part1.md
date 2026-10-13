---
title: "State Machine Diagrams - Part 1"
tags:
  - cs/software-engineering
  - cs/uml
created: 2022-11-07
type: note
---
![[Screenshot 2022-11-07 at 12.53.15.png]]

# Introduction
---
Every object takes a finite number of different stages during its life. State machine diagrams are used as follows:
- To model the possible **states** of a system or object.
- To show how state **transitions** occur as a consequence of events.
- To show what **behaviour** the system or object exhibits in each state.

For example: high-level description of the behaviour of a lecture hall:

![[Screenshot 2022-11-07 at 12.55.04.png]]

Where occupy() and release() are the **transitions** and "free = true"/"free = false" are the **states**.

Another example would be a Digital Clock:
![[Screenshot 2022-11-07 at 12.56.27.png]]

# States
---
They are nodes of the state machine:

![[Screenshot 2022-11-07 at 12.56.59.png|200]]

When a state is active:
- The object is in that state.
- All internal activities specified in this state can be executed, meaning an activity can consist of multiple actions.

entry/Activity(...)
- Executed when the object enters the state.

exit/Activity(...)
- Executed when the object exits the state.

do/Activity(...)
- Executed while the object remains in this state.

![[Screenshot 2022-11-07 at 12.58.46.png|200]]

# Transitions
---
## Syntax
Change from one state to another:

![[Screenshot 2022-11-07 at 12.59.10.png|370]]

- Event (trigger)
    - Exogenous (has an external cause or origin) stimulus.
    - Can trigger a state transition.

- Guard (condition)
    - Boolean expression.
    - If the event occurs, the guard is checked.
    - If the guard is true:
        - All activities in the current state are terminated.
        - Any relevant exit activity is executed.
        - The transition takes place.
    - If the guard is false:
        - No state transition takes place, the event is discarded.

- Activity (effect)
     - Sequence of actions executed during the state transition.

## Types
- Internal:

![[Screenshot 2022-11-07 at 13.11.26.png|300]]

- External:

![[Screenshot 2022-11-07 at 13.11.42.png|300]]

### When do the following transitions take place?
![[Screenshot 2022-11-07 at 13.12.28.png]]

## Sequence of Activity Executions
Assuming $S1$ is active, what is the value of $x$ after $e$ occurred?

![[Screenshot 2022-11-07 at 13.15.10.png|500]]

- $S1$ becomes active, $x$ is set to the value 4.
- $e$ occurs, the guard is checked and evaluates to true.
- $S1$ is left, $x$ is set to 5.
- The transition takes place, $x$ is set to 10.
- $S2$ is entered, $x$ is set to 11.

Registration status of an exam example:

![[Screenshot 2022-11-07 at 13.18.22.png|500]]

# Types of Events
---
## Signal Event
Receipt of a sinal.
- e.g.: `rightmousedown`, `sendSMS(message)`.

## Call Event
Operation call.
-  e.g.: `occupy(user, lectureHall)`, `register(exam)`.

## Time Event
Time-based state transition:
- Relative: based on the time of the occurrence of the event.
    - e.g.: `after(5 seconds)`.
- Absolute
    - e.g.: `when(time==16:00)`, `when(data==20150101)`.

## Any Receive Event
Occurs when any event occurs that does not trigger another transition from the active state:
- Keyword **all**.

## Completion Event
Generated automatically when everything to be done in the current state is complete.

## Change Event
Permanently checking whether a condition becomes true.

E.g.: `when(x > y), after(90min)`.

# Change Event vs Guard
---
![[Screenshot 2022-11-07 at 13.23.25.png|500]]

![[Screenshot 2022-11-07 at 13.23.36.png|500]]

![[Screenshot 2022-11-07 at 13.23.48.png|500]]

# Types of States
---
## Initial State
It is a **pseudo-state**, meaning it is transient (system cannot remain in that state). It is more of a control structure than a real state.

No incoming edges.

- If > 1 outgoing edges:
    - Guards must be mutually exclusive and cover all possible cases to ensure that exactly one target state is reached.

- If initial state becomes active, the object immediately switches to the next state.
    - No events allowed on the outgoing edges (exception: `new()`).

## Final State and Terminate Node
- Final State
    - Real state.
    - Marks the end of the sequence of state.
    - Object can remain in a final state forever.
    - ![[Screenshot 2022-11-07 at 13.29.28.png|25]]

- Terminate Node
    - Pseudo-state.
    - Terminates the state machine.
    - The modelled object ceases to exist (= is deleted).
    - ![[Screenshot 2022-11-07 at 13.30.21.png|25]]

## Decision Node
It is a pseudo-state and is used to model alternative transitions.

![[Screenshot 2022-11-07 at 13.30.54.png|500]]

### Example
![[Screenshot 2022-11-07 at 13.31.12.png|500]]

## Parallelisation and Synchronisation Node
- Parallelisation node
    - Pseudo-state.
    - Splits the control flow into multiple concurrent flows.
    - 1 incoming edge.
    - > 1 outgoing edges.
    - ![[Screenshot 2022-11-07 at 13.32.09.png|70]]

- Synchronisation node
    - Pseudo-state.
    - Merges multiple concurrent flows.
    - > 1 incoming edges.
    - 1 outgoing edge.
    - ![[Screenshot 2022-11-07 at 13.32.50.png|70]]

# Summary
---
![[Screenshot 2022-11-07 at 13.40.00.png]]

![[Screenshot 2022-11-24 at 11.06.15.png]]

---
### Part 2 [[state-machine-diagrams-part2|here]].


> [!nav]
> [[cs-hub|Computer Science]]
