
# ✍️ Jotdown 
 
 > Authors: [Anchita Bora](https://github.com/anchitab), [Jeana Tijerina ](https://github.com/Jeana-T), [Dhruvi Faria](https://github.com/Jeana-T)
 
 > You will be forming a group of **THREE** students and work on an interesting project that you will propose yourself (in this `README.md` document). You can pick any project that you'd like, but it needs ot implement three design patterns. Each of the members in a group is expected to work on at least one design pattern and its test cases. You can, of course, help each other, but it needs to be clear who will be responsible for which pattern and for which general project features.
 
 > ## Expectations
 > * Incorporate **three** distinct design patterns, *two* of the design patterns need to be taught in this course:
 >   * Composite, Strategy, Abstract Factory, Visitor
 > * All three design patterns need to be linked together (it can't be three distinct projects)
 > * Your project should be implemented in C/C++. If you wish to choose anoher programming language (e.g. Java, Python), please discuss with your lab TA to obtain permission.
 > * You can incorporate additional technologies/tools but they must be approved (in writing) by the instructor or the TA.
 > * Each member of the group **must** be committing code regularly and make sure their code is correctly attributed to them. We will be checking attributions to determine if there was equal contribution to the project.

## Project Description
> ## Phase I
> A minimal text editor for students, by students. 
 > * Why is it important or interesting to you?
 >   * Text editors are a crucial part of a computer science student’s workspace. Many rely on this tool not only for coding purposes but also for taking notes, jotting ideas, and even writing assignments. We are avid users of text editors and want to create one for us to use. We want to build a Markdown text editor to allow readability but also allows stylistic elements like bold and italicize. 
 
 > * What languages/tools/technologies do you plan to use? (This list may change over the course of the project)
 >   * [C++](https://www.cplusplus.com/) - An extension of the C programming language optimized for building high-performance applications
 >   * [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Hypertext Markup Language is a markup language for docs displayed in a browser
 >   * [Vanilla JS](https://www.javascript.com/) - Javascript is a scripting language used on both client and server sides allowing pages to be interactive
 >   * [Git](https://git-scm.com/) - A distributed version control system to track updates in code during development within teams
 >   * [Qt](https://www.qt.io/) - Toolkit for creating graphical user interface
 
 > * What will be the input/output of your project?
 >    * The input will be text that users put into the document and the output is the properly formatted text in alliance to Markdown syntax. 

 >   ### Pattern 1: Memento 
 >   #### Features: Undo, Cursor, Scroll Text, Edit History
 >   * Memento enables developers to work on the previous state of objects in the program. This allows features such as undo and edit history to be created as this design pattern can both save and restore the state of its objects. In our project, we plan to implement features such as the scroll position, undo button, cursors coordinates, and edit history. As Memento doesn’t alter the internal structure of the objects, a lot of these features can be created using this design pattern.
 >   ### Pattern 2: Composite 
 >   #### Features: GUI
 >   * Composite enables developers to organize objects into tree structures and navigate these trees as individual objects.  In our program, the user will be able to interact with our project through a GUI or Graphical User Interface. This design pattern allows us to integrate new elements without breaking the previous code. This pattern reduces technical debt as you do not need to use concrete classes or objects since complex and simple elements are all treated uniformly. 
 >   ### Pattern 3: Abstract Factory
 >   #### Features: Copy/Paste, Search/Replace, Nightmode Customization 
 >   * The Abstract Factory Design Pattern essentially helps create families of objects that are related to each other without needing to name their concrete classes. In our program, we hope to implement features such as the ability to customize screen preference, copy/paste function, and enable users to search and replace. This design pattern allows us to integrate new elements without breaking the previous code.


 > ## Phase II
 > In addition to completing the "Class Diagram" section below, you will need to 
 > * Set up your GitHub project board as a Kanban board for the project. It should have columns that map roughly to 
 >   * Backlog, TODO, In progress, In testing, Done
 >   * You can change these or add more if you'd like, but we should be able to identify at least these.
 > * There is no requirement for automation in the project board but feel free to explore those options.
 > * Create an "Epic" (note) for each feature and each design pattern and assign them to the appropriate team member. Place these in the `Backlog` column
 > * Complete your first *sprint planning* meeting to plan out the next 7 days of work.
 >   * Create smaller development tasks as issues and assign them to team members. Place these in the `Backlog` column.
 >   * These cards should represent roughly 7 days worth of development time for your team, taking you until your first meeting with the TA
## Class Diagram
 > Include a class diagram(s) for each design pattern and a description of the diagram(s). This should be in sufficient detail that another group could pick up the project this point and successfully complete it. Use proper OMT notation (as discussed in the course slides). You may combine multiple design patterns into one diagram if you'd like, but it needs to be clear which portion of the diagram represents which design pattern (either in the diagram or in the description). 
 
 > ## Phase III
 > You will need to schedule a check-in with the TA (during lab hours or office hours). Your entire team must be present. 
 > * Before the meeting you should perform a sprint plan like you did in Phase II
 > * In the meeting with your TA you will discuss: 
 >   - How effective your last sprint was (each member should talk about what they did)
 >   - Any tasks that did not get completed last sprint, and how you took them into consideration for this sprint
 >   - Any bugs you've identified and created issues for during the sprint. Do you plan on fixing them in the next sprint or are they lower priority?
 >   - What tasks you are planning for this next sprint.

 > ## Final deliverable
 > All group members will give a demo to the TA during lab time. The TA will check the demo and the project GitHub repository and ask a few questions to all the team members. 
 > Before the demo, you should do the following:
 > * Complete the sections below (i.e. Screenshots, Installation/Usage, Testing)
 > * Plan one more sprint (that you will not necessarily complete before the end of the quarter). Your In-progress and In-testing columns should be empty (you are not doing more work currently) but your TODO column should have a full sprint plan in it as you have done before. This should include any known bugs (there should be some) or new features you would like to add. These should appear as issues/cards on your Kanban board. 
 ## Screenshots
 > Screenshots of the input/output after running your application
 ## Installation/Usage
 > Instructions on installing and running your application
 ## Testing
 > How was your project tested/validated? If you used CI, you should have a "build passing" badge in this README.
 
