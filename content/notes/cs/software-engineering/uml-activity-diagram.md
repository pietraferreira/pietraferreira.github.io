---
title: "Activity Diagram"
tags:
  - cs/software-engineering
  - cs/uml
created: 2022-12-14
type: note
---
---
# Introduction
---
The focus of the activity diagram is the **procedural processing aspects**.

It uses flow-oriented language concepts and it is based on:
- languages for defining business processes.
- established concepts for describing concurrent communicating processes (token concept as found in petri nets).

Concepts and notation variants cover a **broad area of applications**:
- Modelling of object-oriented and non-object-oriented systems.

# Activity
---
It is the specification of user-defined behaviour at different levels of granularity.

Example:
- Definition of the behaviour of an operation in the form of individual instructions.
- Modelling the course of actions of a use case.
- Modelling the functions of a business process.

An activity is a directed graph:
- Nodes: actions and activities.
- Edges: for control and object flow.

The control flow and object flow define the execution.

Optional:
- Parameter.
- Pre and postconditions.

![[Screenshot 2022-12-14 at 12.05.00.png]]

# Action
---
It has a **basic element** to specify user-defined behaviour.

It is **atomic** but can be aborted.

No specific rules for the description of an action. The definition is in natural language or in any programming language.

Process input values to produce output values.

Special notation for predefined types of actions, most importantly:
- Event-based actions.
- Call behaviour actions.

# Edges
---
It connects activities and actions to one another.

Express the execution order.

Types:
- Control flow edges.
    - Defines the order between nodes.
- Object flow edges.
    - Used to exchange data or objects.
    - Express a data/causal dependency between nodes.

Guard (condition):
- Control and object flow only continue if guards in square brackets evaluate to true.

![[Screenshot 2022-12-14 at 12.31.12.png]]

# Token
---
It is a **virtual coordination mechanism** that describes the execution exactly:
- No physical component of the diagram.
- Mechanism that grants the execution permission to actions.

If an action receives a token, the action can be executed. When the action has completed, it passes the token to a subsequent action and the execution of this action is trigged.

Guards can prevent the passing of a token, as they are **stored in the previous node**.

**Control token**: "execution permission" for a node.

**Object token**: transport data + "execution permission".

![[Screenshot 2022-12-14 at 12.34.15.png]]

# Beginning and Termination of Activities
---
![[Screenshot 2022-12-14 at 12.34.56.png]] Initial node:
- Starts the execution of an activity.
- Provides tokens at all outgoing edges.
- Keeps tokens until the successive nodes accept them.
- Multiple initial nodes to model concurrency.

![[Screenshot 2022-12-14 at 12.36.17.png]] Activity final node:
- Ends all flows of an activity.
- First token that reaches the activity final node terminates the entire activity.
    - Concurrent subpaths included.
- Other control and object tokens are deleted.
    - Exception: object tokens that are already present at the output parameters of the activity.

![[Screenshot 2022-12-14 at 12.38.44.png]] Flow final node:
- Ends one execution path of an activity.
- All other tokens of the activity remain unaffected.

# Alternative Paths
---
![[Screenshot 2022-12-14 at 12.44.32.png]]

## Decision Node
---
Used to defined alternative branches.

„Switch point“ for tokens.

Outgoing edges have guards:
- Syntax: \[Boolean expression].
- Token takes **one** branch.
- Guards must be mutually exclusive.
- Predefined: \[else].

![[Screenshot 2022-12-14 at 12.42.25.png]]

Decision behaviour:
- Specify behaviour that is not necessary for the evaluation of the guards.
- Execution must not have side effects.

![[Screenshot 2022-12-14 at 12.42.06.png]]

## Merge Node
---
Used to bring **alternative** subpaths together. It passes the token to the next node.

Combined decision and merge node:

![[Screenshot 2022-12-14 at 12.43.36.png]]

Decision and merge nodes can also be used to model loops:
![[Screenshot 2022-12-14 at 12.44.00.png]]

# Concurrent Paths
## Parallelisation Node
---
Used to split path into concurrent subpaths.

Duplicates token for all outgoing edges, example:

![[Screenshot 2022-12-14 at 12.46.00.png]]

## Synchronisation Node
---
Used to merge concurrent subpaths.

Token processing:
- Waits until tokens are present at all incoming edges.
- Merges all control tokens into one token and passes it on.
- Passes on all object tokens.

Combined parallelisation and synchronisation node:
![[Screenshot 2022-12-14 at 12.47.10.png]]

# Examples
## Equivalent Control Flow
---
![[Screenshot 2022-12-14 at 12.48.30.png]]

## Create and Send Invitations to a Meeting
---
While invitations are printed, already printed invitations are addressed.

When all invitation are addressed, then the invitations are sent.

![[Screenshot 2022-12-14 at 12.48.48.png]]

## Conduct Lecture (Student Perspective)
---
![[Screenshot 2022-12-14 at 12.49.39.png]]

## Token (Control Flow)
---
![[Screenshot 2022-12-14 at 12.50.09.png]]

# Object Node
---
It contains object tokens and represents the exchange of data/objects.

It is the source and target of an object flow edge.

Optional information: type and state.

![[Screenshot 2022-12-14 at 12.51.32.png]]

Notation variant: object node as parameter:
- For activities:
![[Screenshot 2022-12-14 at 12.52.16.png]]

- For actions (“pins”):
![[Screenshot 2022-12-14 at 13.03.57.png]]

## Example
---
![[Screenshot 2022-12-14 at 13.05.07.png]]

## Central Buffer
---
It is for saving and passing on object tokens.

Transient memory, it accepts incoming object tokens from object nodes and passes them on to other object nodes.

When an object token is read from the central buffer, it is deleted from the central buffer and cannot be consumed again.

![[Screenshot 2022-12-14 at 13.08.43.png]]

## Data Store
---
It is for saving and passing on object tokens.

Permanent memory, saves object tokens permanently and passes copies to other nodes.

![[Screenshot 2022-12-14 at 13.09.33.png]]

# Weight of Edges
---
Minimal number of tokens that must be presented for an action to be executed.

Default: 1.

All tokens present have to be consumed: 0 (also `all` or `*`).

![[Screenshot 2022-12-14 at 13.10.26.png]]

# Connector
---
Used if two consecutive actions are far apart in the diagram.

Without connector:
![[Screenshot 2022-12-14 at 13.11.10.png]]

With connector:
![[Screenshot 2022-12-14 at 13.11.18.png]]

# Event-Based Actions
---
To send signals:
- Send signal action:
![[Screenshot 2022-12-14 at 13.12.01.png]]

To accept events:
- Accept event action:
![[Screenshot 2022-12-14 at 13.12.24.png]]

Accept time event action:
![[Screenshot 2022-12-14 at 13.12.44.png]]

## Example
---
![[Screenshot 2022-12-14 at 13.13.01.png]]

# Call Behaviour Action
---
The execution of an action can call an activity.

Content of the called activity can be modelled elsewhere.

Advantages:
- Model becomes clearer.
- Reusability.

![[Screenshot 2022-12-14 at 13.14.10.png]]

# Partition
---
"Swimlane". Graphically or textual. 

It allows the grouping of nodes and edges of an activity due to responsibilities.

Responsibilities reflect organisational units or roles.

Makes the diagram more structured.

Does not change the execution semantics.

Example:
- partitions `Student` and `Institute Employee` (with sub-partitions `Professor` and `Secretary`).

![[Screenshot 2022-12-14 at 13.19.19.png]]

![[Screenshot 2022-12-14 at 13.19.35.png]]

## Multidimensional Partitions
---
Graphical notation vs Textual notation:

![[Screenshot 2022-12-14 at 13.20.17.png]]

### Example: Issue Student ID on Paper
---
![[Screenshot 2022-12-14 at 13.20.50.png]]

- Control flow (green) and object flow (red) in one activity diagram:
![[Screenshot 2022-12-14 at 13.21.03.png]]

# Exception Handling
Exception Handler
---
Predefined exceptions.

Defining how the system has to react in a specific error situation.

The exception handler replaces the action where the error occurred.

![[Screenshot 2022-12-16 at 10.25.55.png]]

If the error **e** occurs:
- All tokens in `Action A` are deleted.
- The exception handler is activated.
- The exception handler is executed instead of  `Action A`.
- Execution then continues regularly.

### Example
---
![[Screenshot 2022-12-16 at 10.27.28.png]]

## Interruptible Activity Region
---
Defining a group of actions whose execution is to be terminated immediately if a specific event occurs. In that case, some other behaviour is executed.

![[Screenshot 2022-12-16 at 10.34.48.png]]

If **E** occurs while **B** or **C** are executed:
- Exception handling is activated.
- All control tokens within the dashed rectangle (= within **B** and **C**) are deleted.
- **D** is activated and executed.

No "jumping back" to the regular execution!

### Example
---
![[Screenshot 2022-12-16 at 10.36.33.png]]

# Notation Elements
---
![[Screenshot 2022-12-16 at 10.37.00.png]]

![[Screenshot 2022-12-16 at 10.37.10.png]]

![[Screenshot 2022-12-16 at 10.37.22.png]]

![[Screenshot 2022-12-16 at 10.37.30.png]]

![[Screenshot 2022-12-16 at 10.37.39.png]]


> [!nav]
> [[cs-hub|Computer Science]]
