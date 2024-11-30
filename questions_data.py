questions = [
    {
        'type': 'mcq',
        'question': 'Which of the following is **NOT** a primitive data type in Java?',
        'options': ['int', 'boolean', 'String', 'char', 'double'],
        'answer': 'C',
        'explanation': 'String is a class in Java, not a primitive data type.'
    },
    {
        'type': 'mcq',
        'question': 'What is the output of the following code snippet?\n\n```java\nint x = 5;\nSystem.out.println(++x);\n```',
        'options': ['4', '5', '6', '7', 'Compilation error'],
        'answer': 'C',
        'explanation': 'The prefix increment operator increments x before using it, so x becomes 6.'
    },
    {
        'type': 'mcq',
        'question': 'Given the array declaration:\n\n```java\nint[] numbers = new int[5];\n```\n\nWhat is the default value of `numbers[2]`?',
        'options': ['0', 'null', 'Garbage value', 'Undefined', 'Compilation error'],
        'answer': 'A',
        'explanation': 'Integer array elements are initialized to 0 by default.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following statements about Java arrays is **FALSE**?',
        'options': [
            'The array size can never change once it is set.',
            'Arrays are contiguous in memory.',
            'Default value for object arrays is null.',
            'Arrays can hold primitive data types and objects.',
            'Arrays can be dynamically resized after creation.'
        ],
        'answer': 'E',
        'explanation': 'In Java, arrays cannot be dynamically resized after creation.'
    },
    {
        'type': 'mcq',
        'question': 'Given the following code, what will be the output?\n\n```java\nString s1 = "Hello";\nString s2 = "Hello";\nSystem.out.println(s1 == s2);\n```',
        'options': ['true', 'false', 'Compilation error', 'Runtime error', 'Depends on the JVM'],
        'answer': 'A',
        'explanation': 'String literals refer to the same object in the string pool, so s1 == s2 is true.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is a valid way to get the length of an array named `arr`?',
        'options': ['arr.length()', 'arr.size()', 'arr.length', 'arr.getLength()', 'arr.getSize()'],
        'answer': 'C',
        'explanation': 'Arrays have a property called length (without parentheses).'
    },
    {
        'type': 'mcq',
        'question': 'What will be the output of the following code?\n\n```java\nSystem.out.println("Hello\\nWorld");\n```',
        'options': ['Hello World', 'Hello\\nWorld', 'Hello\nWorld', 'Hello\\tWorld', 'Compilation error'],
        'answer': 'C',
        'explanation': 'The \\n is an escape sequence for a new line.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following keywords is **NOT** a reserved keyword in Java?',
        'options': ['assert', 'enum', 'const', 'goto', 'friend'],
        'answer': 'E',
        'explanation': '`friend` is not a reserved keyword in Java; it is in C++.'
    },
    {
        'type': 'mcq',
        'question': 'What is the size of an `int` data type in Java?',
        'options': ['8 bits', '16 bits', '32 bits', '64 bits', 'Size depends on the platform'],
        'answer': 'C',
        'explanation': 'An int in Java is always 32 bits, regardless of the platform.'
    },
    {
        'type': 'mcq',
        'question': 'Which method is used to read an integer input from the user using a Scanner object named `sc`?',
        'options': ['sc.readInt()', 'sc.nextInt()', 'sc.getInt()', 'sc.inputInt()', 'sc.scanInt()'],
        'answer': 'B',
        'explanation': '`nextInt()` reads the next integer from the input.'
    },
    {
        'type': 'mcq',
        'question': 'In Java, what is the result of the expression `10 / 4` when both operands are integers?',
        'options': ['2.5', '2', '3', '2.0', 'Compilation error'],
        'answer': 'C',
        'explanation': 'Integer division discards the decimal part; 10 / 4 = 2.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following statements is **TRUE** about Java memory management?',
        'options': [
            'Java requires manual deallocation of memory.',
            'Java uses pointers for memory management.',
            'Java has a garbage collector that handles deallocation.',
            'Java objects are stored on the stack.',
            'Java does not manage memory automatically.'
        ],
        'answer': 'C',
        'explanation': 'Java uses a garbage collector to automatically manage memory.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following correctly defines a method that can accept a variable number of integer arguments?',
        'options': [
            'void method(int... numbers)',
            'void method(int[] numbers)',
            'void method(int numbers...)',
            'void method(...int numbers)',
            'void method(int numbers[]...)'
        ],
        'answer': 'A',
        'explanation': 'The syntax `int... numbers` allows for a variable number of int arguments.'
    },
    {
        'type': 'mcq',
        'question': 'What is the correct way to declare a constant double variable named `PI` with a value of `3.14159`?',
        'options': [
            'final double PI = 3.14159;',
            'const double PI = 3.14159;',
            'static double PI = 3.14159;',
            'double final PI = 3.14159;',
            'double PI = final 3.14159;'
        ],
        'answer': 'A',
        'explanation': 'In Java, the `final` keyword is used to declare constants.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following statements about the `this` keyword in Java is **FALSE**?',
        'options': [
            'this refers to the current object.',
            'this can be used to call another constructor in the same class.',
            'this can be used in a static method.',
            'this can be used to distinguish between instance variables and parameters.',
            'this is a reference to the object on which the method was invoked.'
        ],
        'answer': 'C',
        'explanation': '`this` cannot be used in static methods because static methods do not belong to an instance.'
    },
    {
        'type': 'mcq',
        'question': 'What will be the output of the following code?\n\n```java\nInteger num1 = new Integer(128);\nInteger num2 = new Integer(128);\nSystem.out.println(num1 == num2);\n```',
        'options': ['true', 'false', 'Compilation error', 'Runtime error', 'Cannot be determined'],
        'answer': 'B',
        'explanation': 'Using `==` compares object references. Since they are different objects, it returns false.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is the correct entry point of a Java application?',
        'options': [
            'public void main(String args[])',
            'static public void main(String[] args)',
            'public static void main(String args)',
            'public static int main(String[] args)',
            'private static void main(String[] args)'
        ],
        'answer': 'B',
        'explanation': 'The correct main method signature is `public static void main(String[] args)`; the order of `public` and `static` can be interchanged.'
    },
    {
        'type': 'mcq',
        'question': 'Which package is automatically imported into every Java program?',
        'options': ['java.util', 'java.io', 'java.lang', 'java.awt', 'java.math'],
        'answer': 'C',
        'explanation': '`java.lang` is automatically imported into every Java program.'
    },
    {
        'type': 'mcq',
        'question': 'What is autoboxing in Java?',
        'options': [
            'Automatically converting a primitive type to its corresponding wrapper object.',
            'Automatically converting a wrapper object to its corresponding primitive type.',
            'Automatically casting between incompatible types.',
            'Automatically creating arrays from individual elements.',
            'Automatically generating getters and setters.'
        ],
        'answer': 'A',
        'explanation': 'Autoboxing is the automatic conversion of primitive types to their corresponding wrapper classes.'
    },
    {
        'type': 'mcq',
        'question': 'Given the code snippet:\n\n```java\npublic class Calculator {\n    public static int add(int a, int b) {\n        return a + b;\n    }\n}\n```\n\nWhich of the following is the correct way to call the `add` method without creating an instance of `Calculator`?',
        'options': [
            'Calculator calc = new Calculator(); calc.add(3, 4);',
            'Calculator.add(3, 4);',
            'add(3, 4);',
            'calc.add(3, 4);',
            'new Calculator().add(3, 4);'
        ],
        'answer': 'B',
        'explanation': 'Since `add` is a static method, it can be called using the class name without creating an instance.'
    },
    # Continue adding the rest of your questions with 'type' and 'explanation'
    # For brevity, I'll include a few more examples
    {
        'type': 'mcq',
        'question': 'Which of the following code snippets demonstrates **upcasting** in Java?',
        'options': [
            'Dog dog = new Animal();',
            'Animal animal = new Dog();',
            'Dog dog = (Dog) new Animal();',
            'Animal animal = new Animal();',
            'Dog dog = new Dog();'
        ],
        'answer': 'B',
        'explanation': 'Upcasting is casting a subclass object to a superclass reference.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following statements about Java interfaces is **TRUE**?',
        'options': [
            'Interfaces can have instance fields.',
            'Interfaces can be instantiated directly.',
            'A class can implement multiple interfaces.',
            'Interfaces can extend classes.',
            'All methods in interfaces must be private.'
        ],
        'answer': 'C',
        'explanation': 'Java allows a class to implement multiple interfaces.'
    },
    {
        'type': 'mcq',
        'question': 'Which keyword is used to check if an object is of a specific type at runtime?',
        'options': ['cast', 'instanceof', 'implements', 'extends', 'as'],
        'answer': 'B',
        'explanation': 'The `instanceof` operator checks if an object is of a specific type at runtime.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following best describes **method overriding** in Java?',
        'options': [
            'Defining multiple methods with the same name but different parameters in the same class.',
            'Changing the return type of a method in a subclass.',
            'Providing a new implementation for a method inherited from a superclass.',
            'Using the final keyword to prevent method inheritance.',
            'Having multiple methods with the same name and parameters in different classes.'
        ],
        'answer': 'C',
        'explanation': 'Method overriding allows a subclass to provide a specific implementation of a method already provided by its superclass.'
    },
    {
        'type': 'mcq',
        'question': 'Which design pattern ensures that a class has only one instance and provides a global point of access to it?',
        'options': ['Factory', 'Singleton', 'Observer', 'Decorator', 'Strategy'],
        'answer': 'B',
        'explanation': 'The Singleton pattern restricts the instantiation of a class to one object.'
    },
    {
        'type': 'mcq',
        'question': 'What exception is thrown when an application attempts to use `null` in a case where an object is required?',
        'options': [
            'NullPointerException',
            'IllegalArgumentException',
            'ClassCastException',
            'ArrayIndexOutOfBoundsException',
            'NumberFormatException'
        ],
        'answer': 'A',
        'explanation': 'A `NullPointerException` is thrown when an application tries to use `null` where an object is required.'
    },
    {
        'type': 'mcq',
        'question': 'Which method must be implemented when creating a custom exception in Java?',
        'options': [
            'public String getMessage()',
            'public void printStackTrace()',
            'public void handleException()',
            'Constructors matching superclass constructors',
            'No methods need to be implemented'
        ],
        'answer': 'D',
        'explanation': 'When creating a custom exception, you should provide constructors that match the superclass.'
    },
    {
        'type': 'mcq',
        'question': 'Which keyword is used to prevent a method from being overridden in a subclass?',
        'options': ['static', 'final', 'abstract', 'private', 'protected'],
        'answer': 'B',
        'explanation': 'The `final` keyword prevents a method from being overridden.'
    },
    {
        'type': 'mcq',
        'question': 'What is the purpose of the `volatile` keyword in Java?',
        'options': [
            'To indicate that a variable can be modified asynchronously by multiple threads.',
            'To make a variable constant.',
            'To synchronize a method.',
            'To prevent a variable from being serialized.',
            'To declare a variable that can change type at runtime.'
        ],
        'answer': 'A',
        'explanation': '`volatile` tells the JVM that a variable may be modified by multiple threads.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is a checked exception in Java?',
        'options': [
            'NullPointerException',
            'ArrayIndexOutOfBoundsException',
            'ClassNotFoundException',
            'ArithmeticException',
            'IllegalArgumentException'
        ],
        'answer': 'C',
        'explanation': '`ClassNotFoundException` is a checked exception that must be declared or handled.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is a feature of Java\'s “Write Once, Run Anywhere” (WORA) philosophy?',
        'options': [
            'Java programs are compiled to native machine code.',
            'Java programs can run on any device with a Java Virtual Machine (JVM).',
            'Java requires manual memory management.',
            'Java is only compatible with Windows operating systems.',
            'Java uses pointers for memory access.'
        ],
        'answer': 'B',
        'explanation': 'Java programs are compiled into bytecode, which runs on the JVM, making them platform-independent.'
    },
    {
        'type': 'mcq',
        'question': 'In Java, which of the following is NOT a primitive data type?',
        'options': ['int', 'char', 'boolean', 'String', 'double'],
        'answer': 'D',
        'explanation': 'String is not a primitive data type; it is a class in Java.'
    },
    {
        'type': 'mcq',
        'question': 'What is the default value of a boolean array in Java?',
        'options': ['true', 'false', 'null', '0', '1'],
        'answer': 'B',
        'explanation': 'Boolean arrays default to false for all elements.'
    },
    {
        'type': 'mcq',
        'question': 'Which keyword is used to create a package in Java?',
        'options': ['import', 'package', 'define', 'module', 'namespace'],
        'answer': 'B',
        'explanation': 'The `package` keyword is used to declare a package in Java.'
    },
    {
        'type': 'mcq',
        'question': 'How do you import the `ArrayList` class from the `java.util` package?',
        'options': [
            'import java.util.ArrayList;',
            'import java.ArrayList;',
            'import util.ArrayList;',
            'import java.util.*;',
            'Both A and D'
        ],
        'answer': 'E',
        'explanation': 'Both `import java.util.ArrayList;` and `import java.util.*;` correctly import the `ArrayList` class.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following statements about encapsulation is FALSE?',
        'options': [
            'Encapsulation hides the internal state of an object.',
            'Encapsulation allows controlled access through methods.',
            'Encapsulation promotes code reusability and maintenance.',
            'Encapsulation allows direct access to class fields.',
            'Encapsulation is a fundamental OOP principle.'
        ],
        'answer': 'D',
        'explanation': 'Encapsulation does not allow direct access to class fields; it restricts access and provides controlled methods.'
    },
    {
        'type': 'mcq',
        'question': 'What is the purpose of the `this` keyword in Java?',
        'options': [
            'To refer to the current object instance.',
            'To call a superclass method.',
            'To create a new object.',
            'To declare a static method.',
            'To terminate a method.'
        ],
        'answer': 'A',
        'explanation': 'The `this` keyword refers to the current object instance, allowing access to its members.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following best describes a constructor in Java?',
        'options': [
            'A method that must have a return type.',
            'A special method used to initialize objects.',
            'A method that can be inherited.',
            'A method that can be overridden.',
            'A static method used for utility purposes.'
        ],
        'answer': 'B',
        'explanation': 'A constructor is a special method used to initialize new objects of a class.'
    },
    {
        'type': 'mcq',
        'question': 'Which access modifier makes a class member accessible only within its own package and subclasses?',
        'options': ['private', 'public', 'protected', 'default', 'final'],
        'answer': 'C',
        'explanation': 'The `protected` access modifier allows access within the same package and subclasses.'
    },
    {
        'type': 'mcq',
        'question': 'What is the result of casting a double value 9.99 to an integer in Java?',
        'options': ['10', '9.99', '0', 'Compilation error', '9'],
        'answer': 'E',
        'explanation': 'Casting a double to an int truncates the decimal part, resulting in 9.'
    },
    {
        'type': 'mcq',
        'question': 'In Java, which term describes a class having instance fields that are other objects?',
        'options': ['Inheritance', 'Composition', 'Polymorphism', 'Abstraction', 'Encapsulation'],
        'answer': 'B',
        'explanation': 'Composition is when a class includes instances of other classes as fields.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following statements about interfaces in Java is TRUE?',
        'options': [
            'A class can extend multiple interfaces.',
            'Interfaces can have constructors.',
            'Interfaces can contain implemented methods in Java 8 and later.',
            'Interfaces cannot have constants.',
            'Interfaces are instantiated directly.'
        ],
        'answer': 'C',
        'explanation': 'Since Java 8, interfaces can have default and static methods with implementations.'
    },
    {
        'type': 'mcq',
        'question': 'What does polymorphism in Java allow you to do?',
        'options': [
            'Create multiple classes with the same name.',
            'Use objects of different classes through the same interface.',
            'Inherit from multiple classes.',
            'Automatically convert between primitive types.',
            'Declare variables without specifying their type.'
        ],
        'answer': 'B',
        'explanation': 'Polymorphism allows using objects of different classes through a common interface or superclass.'
    },
    {
        'type': 'mcq',
        'question': 'How do you call a non-static method in Java?',
        'options': [
            'Using the class name directly.',
            'Without creating an instance of the class.',
            'By creating an instance of the class first.',
            'Non-static methods cannot be called.',
            'Using the \'static\' keyword.'
        ],
        'answer': 'C',
        'explanation': 'Non-static methods require an instance of the class to be called.'
    },
    {
        'type': 'mcq',
        'question': 'What is upcasting in Java?',
        'options': [
            'Casting a superclass reference to a subclass type.',
            'Casting a subclass reference to a superclass type.',
            'Casting between unrelated classes.',
            'Casting primitive types.',
            'Casting objects during garbage collection.'
        ],
        'answer': 'B',
        'explanation': 'Upcasting is casting a subclass reference to a superclass type.'
    },
    {
        'type': 'mcq',
        'question': 'What is the risk associated with downcasting in Java?',
        'options': [
            'It always fails at compile time.',
            'It can lead to a ClassCastException at runtime if the object is not of the target subclass.',
            'It is not allowed in Java.',
            'It can change the object\'s type permanently.',
            'It automatically converts primitives to objects.'
        ],
        'answer': 'B',
        'explanation': 'Downcasting can lead to ClassCastException if the object isn\'t actually an instance of the target subclass.'
    },
    {
        'type': 'mcq',
        'question': 'Which characteristic is essential for implementing the Singleton pattern in Java?',
        'options': [
            'Allowing multiple instances of the class.',
            'Providing a public constructor.',
            'Having a private static instance of the class.',
            'Using abstract classes.',
            'Implementing an interface.'
        ],
        'answer': 'C',
        'explanation': 'Singleton pattern requires a private static instance variable to ensure only one instance exists.'
    },
    {
        'type': 'mcq',
        'question': 'What is the primary purpose of the Factory design pattern in Java?',
        'options': [
            'To restrict class instantiation.',
            'To provide a way to create objects without specifying the exact class of object that will be created.',
            'To manage multiple threads.',
            'To control access to resources.',
            'To enhance performance.'
        ],
        'answer': 'B',
        'explanation': 'Factory pattern abstracts object creation, allowing creation without specifying exact class.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is TRUE about Java interfaces compared to abstract classes?',
        'options': [
            'Interfaces can have constructors.',
            'A class can implement multiple interfaces but can extend only one abstract class.',
            'Interfaces can have instance fields.',
            'Abstract classes cannot have methods with implementations.',
            'Interfaces cannot be nested.'
        ],
        'answer': 'B',
        'explanation': 'A class can implement multiple interfaces but can extend only one class (abstract or concrete).'
    },
    {
        'type': 'mcq',
        'question': 'What does the \'instanceof\' keyword do in Java?',
        'options': [
            'Casts an object to a specific type.',
            'Checks if an object is an instance of a specific class or interface.',
            'Creates a new instance of a class.',
            'Declares a new variable.',
            'Overrides a method.'
        ],
        'answer': 'B',
        'explanation': '\'instanceof\' checks whether an object is an instance of a specified type.'
    },
    {
        'type': 'mcq',
        'question': 'What differentiates method overloading from method overriding in Java?',
        'options': [
            'Overloading involves methods with the same name but different return types, while overriding involves same name and parameters.',
            'Overloading occurs in the same class, while overriding happens in subclasses.',
            'Overloading requires inheritance, overriding does not.',
            'Overloading is resolved at runtime, overriding at compile time.',
            'There is no difference.'
        ],
        'answer': 'B',
        'explanation': 'Overloading is multiple methods with the same name but different parameters in the same class; overriding is subclass providing its own implementation of a superclass method.'
    },
    {
        'type': 'mcq',
        'question': 'What is a key difference between an abstract class and an interface in Java?',
        'options': [
            'Abstract classes cannot have any method implementations.',
            'Interfaces can have constructors.',
            'Abstract classes can have state (instance variables), while interfaces cannot.',
            'Interfaces can inherit from classes, abstract classes cannot.',
            'Abstract classes cannot have static methods.'
        ],
        'answer': 'C',
        'explanation': 'Abstract classes can have instance variables to maintain state; interfaces cannot have instance variables (only constants).'
    },
    {
        'type': 'mcq',
        'question': 'When would you prefer composition over inheritance in Java?',
        'options': [
            'When you need to extend functionality of a class.',
            'When you want to achieve a has-a relationship.',
            'When you need to override a method.',
            'When multiple inheritance is required.',
            'When classes are final.'
        ],
        'answer': 'B',
        'explanation': 'Composition models a has-a relationship and is preferred for flexibility over inheritance\'s is-a.'
    },
    {
        'type': 'mcq',
        'question': 'By convention, how should Java interface names typically end?',
        'options': ['-ator', '-able', '-ing', '-er', '-ment'],
        'answer': 'B',
        'explanation': 'Interfaces are often named with \'-able\' suffix (e.g., Iterable, Serializable).'
    },
    {
        'type': 'mcq',
        'question': 'Which method is NOT part of the Java Iterator interface?',
        'options': ['hasNext()', 'next()', 'remove()', 'reset()', 'None of the above'],
        'answer': 'D',
        'explanation': 'Iterator interface includes hasNext(), next(), and remove(); reset() is not part of it.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following classes implements the List interface in Java?',
        'options': ['HashSet', 'LinkedList', 'TreeMap', 'PriorityQueue', 'Vector'],
        'answer': 'B',
        'explanation': 'LinkedList implements the List interface.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is NOT a method defined in the Java Map interface?',
        'options': ['put(key, value)', 'get(key)', 'keySet()', 'add(key, value)', 'entrySet()'],
        'answer': 'D',
        'explanation': 'Map interface does not have an add() method; use put() to add key-value pairs.'
    },
    {
        'type': 'mcq',
        'question': 'How do you remove the last element returned by an Iterator in Java?',
        'options': ['iterator.removeLast()', 'iterator.delete()', 'iterator.remove()', 'remove(current())', 'None of the above'],
        'answer': 'C',
        'explanation': 'The remove() method removes the last element returned by next().' 
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is an example of object composition in Java?',
        'options': [
            'class Car extends Vehicle {}',
            'class Engine {} class Car { private Engine engine; }',
            'class Bicycle {}',
            'class Boat implements Vessel {}',
            'class Plane extends Aircraft {}'
        ],
        'answer': 'B',
        'explanation': 'Car has an Engine instance as a field, illustrating composition.'
    },
    {
        'type': 'mcq',
        'question': 'What annotation is used in Java to indicate that a method is overriding a superclass method?',
        'options': ['@Override', '@Super', '@OverrideMethod', '@Overloaded', '@OverrideClass'],
        'answer': 'A',
        'explanation': 'The @Override annotation indicates that the method is meant to override a superclass method.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is a way to prevent instantiation of a class from outside in the Singleton pattern?',
        'options': [
            'Make the class abstract.',
            'Provide a private constructor.',
            'Make the class final.',
            'Use synchronized keyword on methods.',
            'Inherit from a base class.'
        ],
        'answer': 'B',
        'explanation': 'A private constructor prevents external instantiation.'
    },
    {
        'type': 'mcq',
        'question': 'What advantage does the Factory pattern provide in Java?',
        'options': [
            'It allows for faster object creation.',
            'It centralizes object creation logic.',
            'It reduces memory consumption.',
            'It allows multiple inheritance.',
            'It enables direct access to object fields.'
        ],
        'answer': 'B',
        'explanation': 'Factory pattern centralizes the object creation logic, improving scalability and maintainability.'
    },
    {
        'type': 'mcq',
        'question': 'Given two classes implementing the same interface, what allows polymorphism to work in Java?',
        'options': [
            'Both classes must have the same methods with the same signatures.',
            'Both classes must extend a common superclass.',
            'Both classes must be in the same package.',
            'Both classes must not have any instance variables.',
            'Interface methods must be private.'
        ],
        'answer': 'A',
        'explanation': 'Polymorphism relies on classes implementing the same interface methods.'
    },
    {
        'type': 'mcq',
        'question': 'Can an abstract class in Java be instantiated directly?',
        'options': ['Yes, like any other class.', 'No, because it is incomplete.', 'Only if all abstract methods are implemented.', 'Only within its package.', 'Only using reflection.'],
        'answer': 'B',
        'explanation': 'Abstract classes cannot be instantiated directly.'
    },
    # ...existing code...
    # Exceptions, Reflection, and Inner Classes (M5)
    {
        'type': 'mcq',
        'question': 'Which of the following is a checked exception in Java?',
        'options': [
            'NullPointerException',
            'ArithmeticException',
            'IOException',
            'ArrayIndexOutOfBoundsException',
            'IllegalArgumentException'
        ],
        'answer': 'C',
        'explanation': '`IOException` is a checked exception that must be either caught or declared in the method signature.'
    },
    {
        'type': 'mcq',
        'question': 'What is the superclass of all exceptions in Java?',
        'options': [
            'Exception',
            'Throwable',
            'RuntimeException',
            'Error',
            'Object'
        ],
        'answer': 'B',
        'explanation': '`Throwable` is the superclass of all errors and exceptions in Java.'
    },
    {
        'type': 'mcq',
        'question': 'Which block is always executed regardless of whether an exception is thrown or not?',
        'options': [
            'try',
            'catch',
            'finally',
            'throw',
            'throws'
        ],
        'answer': 'C',
        'explanation': 'The `finally` block is always executed after the `try` and `catch` blocks, used for cleanup tasks.'
    },
    {
        'type': 'mcq',
        'question': 'How do you create a custom checked exception in Java?',
        'options': [
            'public class CustomException extends RuntimeException {}',
            'public class CustomException extends Exception {}',
            'public class CustomException implements Throwable {}',
            'public class CustomException extends Error {}',
            'public class CustomException extends Throwable {}'
        ],
        'answer': 'B',
        'explanation': 'Custom checked exceptions should extend the `Exception` class.'
    },
    {
        'type': 'mcq',
        'question': 'What keyword is used to explicitly throw an exception in Java?',
        'options': [
            'throw',
            'throws',
            'throwable',
            'exception',
            'catch'
        ],
        'answer': 'A',
        'explanation': 'The `throw` keyword is used to explicitly throw an exception.'
    },
    {
        'type': 'mcq',
        'question': 'Which method in the `Throwable` class returns a detailed message about the exception?',
        'options': [
            'getMessage()',
            'toString()',
            'printStackTrace()',
            'getCause()',
            'initCause()'
        ],
        'answer': 'A',
        'explanation': '`getMessage()` returns the detail message string of the throwable.'
    },
    {
        'type': 'mcq',
        'question': 'What is reflection in Java used for?',
        'options': [
            'To handle exceptions dynamically.',
            'To inspect and manipulate classes, methods, and fields at runtime.',
            'To perform input/output operations.',
            'To create graphical user interfaces.',
            'To manage memory allocation.'
        ],
        'answer': 'B',
        'explanation': 'Reflection allows inspection and manipulation of classes, methods, and fields at runtime.'
    },
    {
        'type': 'mcq',
        'question': 'Which class in Java is primarily used for reflection?',
        'options': [
            'Class',
            'Object',
            'Reflect',
            'Method',
            'Field'
        ],
        'answer': 'A',
        'explanation': '`Class` objects are central to Java Reflection, providing methods to inspect class details.'
    },
    {
        'type': 'mcq',
        'question': 'How can you invoke a method using reflection in Java?',
        'options': [
            'Using the `invokeMethod()` function.',
            'Using the `Method.invoke()` method.',
            'Using the `callMethod()` function.',
            'Using the `execute()` method.',
            'Using the `runMethod()` function.'
        ],
        'answer': 'B',
        'explanation': 'The `invoke()` method of the `Method` class is used to invoke a method via reflection.'
    },
    {
        'type': 'mcq',
        'question': 'What is an inner class in Java?',
        'options': [
            'A class defined within another class.',
            'A subclass that extends another class.',
            'A class that implements an interface.',
            'A class that cannot be instantiated.',
            'A class defined in the same package.'
        ],
        'answer': 'A',
        'explanation': 'An inner class is a class defined within the scope of another class.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following can an inner class access?',
        'options': [
            'Only static members of the outer class.',
            'Only public members of the outer class.',
            'All members of the outer class, including private ones.',
            'Only methods, not fields of the outer class.',
            'None of the outer class members.'
        ],
        'answer': 'C',
        'explanation': 'Inner classes have access to all members of the outer class, including private ones.'
    },
    {
        'type': 'mcq',
        'question': 'How do you instantiate a non-static inner class in Java?',
        'options': [
            'OuterClass.InnerClass inner = new OuterClass.InnerClass();',
            'OuterClass outer = new OuterClass(); OuterClass.InnerClass inner = outer.new InnerClass();',
            'InnerClass inner = new InnerClass();',
            'OuterClass.InnerClass inner = OuterClass.new InnerClass();',
            'InnerClass inner = OuterClass.InnerClass.newInstance();'
        ],
        'answer': 'B',
        'explanation': 'A non-static inner class requires an instance of the outer class to be instantiated.'
    },
    {
        'type': 'mcq',
        'question': 'What is an anonymous inner class in Java?',
        'options': [
            'An inner class without access modifiers.',
            'An inner class defined without a name typically used for one-time use.',
            'An inner class defined outside of any method.',
            'An inner class that is static.',
            'An inner class that extends another class.'
        ],
        'answer': 'B',
        'explanation': 'Anonymous inner classes are declared without a name and are typically used for one-time implementations.'
    },
    {
        'type': 'mcq',
        'question': 'Which keyword is used to declare a static inner class in Java?',
        'options': [
            'static',
            'final',
            'abstract',
            'public',
            'private'
        ],
        'answer': 'A',
        'explanation': 'The `static` keyword is used to declare a static inner class.'
    },
    {
        'type': 'mcq',
        'question': 'Can a static inner class access non-static members of the outer class?',
        'options': [
            'Yes, directly.',
            'Yes, indirectly through an instance of the outer class.',
            'No, it cannot access them at all.',
            'Only if it is in the same package.',
            'Only if the outer class methods are static.'
        ],
        'answer': 'B',
        'explanation': 'A static inner class cannot directly access non-static members but can through an instance of the outer class.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is true about the `try-catch-finally` block in Java?',
        'options': [
            'The `finally` block is optional.',
            'The `catch` block must always follow the `finally` block.',
            'You can have multiple `finally` blocks for a single `try` block.',
            'A `try` block cannot exist without a `catch` block.',
            'The `finally` block executes only if an exception is caught.'
        ],
        'answer': 'A',
        'explanation': 'The `finally` block is optional and is used for cleanup code that should run regardless of whether an exception was thrown.'
    },
    {
        'type': 'mcq',
        'question': 'Which exception is thrown when attempting to access an array with an invalid index?',
        'options': [
            'NullPointerException',
            'ArrayIndexOutOfBoundsException',
            'IllegalArgumentException',
            'ClassCastException',
            'NumberFormatException'
        ],
        'answer': 'B',
        'explanation': '`ArrayIndexOutOfBoundsException` is thrown when an array has been accessed with an illegal index.'
    },
    {
        'type': 'mcq',
        'question': 'What is the purpose of the `throws` keyword in a method signature?',
        'options': [
            'To throw an exception explicitly.',
            'To declare that the method might throw certain exceptions.',
            'To catch exceptions thrown by the method.',
            'To create a new exception.',
            'To handle exceptions within the method.'
        ],
        'answer': 'B',
        'explanation': 'The `throws` keyword declares that the method may throw specified exceptions, which must be handled by the caller.'
    },
    {
        'type': 'mcq',
        'question': 'Which method in the `Class` class returns an array of all declared methods of the class?',
        'options': [
            'getMethods()',
            'getDeclaredMethods()',
            'getMethodNames()',
            'getAllMethods()',
            'getMethodList()'
        ],
        'answer': 'B',
        'explanation': '`getDeclaredMethods()` returns an array of all the methods declared by the class, including private methods.'
    },
    {
        'type': 'mcq',
        'question': 'How can you change the value of a private field using reflection in Java?',
        'options': [
            'It is not possible to change private fields using reflection.',
            'By using the `setAccessible(true)` method on the `Field` object.',
            'By subclassing the class containing the private field.',
            'By using the `setPrivate()` method on the `Field` object.',
            'By making the field public at runtime.'
        ],
        'answer': 'B',
        'explanation': 'Using `setAccessible(true)` allows reflection to bypass access control checks and modify private fields.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following best describes the `invoke` method in Java Reflection?',
        'options': [
            'It creates a new instance of a class.',
            'It invokes a constructor of a class.',
            'It invokes a method on a given object.',
            'It retrieves the value of a field.',
            'It changes the access level of a method.'
        ],
        'answer': 'C',
        'explanation': 'The `invoke` method is used to call a method on a given object with specified parameters.'
    },
    {
        'type': 'mcq',
        'question': 'What is the primary purpose of a layout manager in GUI development?',
        'options': [
            'Handle user authentication',
            'Manage the layout of components',
            'Perform database operations',
            'Manage network connections'
        ],
        'answer': 'Manage the layout of components'
    },
    {
        'type': 'mcq',
        'question': 'Which layout manager arranges components in equally sized rows and columns?',
        'options': [
            'BorderLayout',
            'FlowLayout',
            'GridLayout',
            'BoxLayout'
        ],
        'answer': 'GridLayout'
    },
    {
        'type': 'mcq',
        'question': 'In Java Swing, which layout manager allows for more fine-grained customization than GridLayout?',
        'options': [
            'FlowLayout',
            'BorderLayout',
            'BoxLayout',
            'GridBagLayout'
        ],
        'answer': 'GridBagLayout'
    },
    {
        'type': 'mcq',
        'question': 'What does the wildcard \'?\' represent in Java Generics?',
        'options': [
            'A specific type',
            'Any type',
            'A bounded type',
            'A primitive type'
        ],
        'answer': 'Any type'
    },
    {
        'type': 'mcq',
        'question': 'How do Generics improve code safety?',
        'options': [
            'By allowing dynamic type checks at runtime',
            'By enforcing type constraints at compile time',
            'By enabling multiple inheritance',
            'By reducing memory usage'
        ],
        'answer': 'By enforcing type constraints at compile time'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is NOT a type of layout manager in Java Swing?',
        'options': [
            'BorderLayout',
            'FlowLayout',
            'StackLayout',
            'BoxLayout'
        ],
        'answer': 'StackLayout'
    },
    {
        'type': 'mcq',
        'question': 'What is the role of an event listener in the Java event model?',
        'options': [
            'To generate events',
            'To store event data',
            'To respond to events',
            'To ignore events'
        ],
        'answer': 'To respond to events'
    },
    {
        'type': 'mcq',
        'question': 'Which layout manager stacks components and shows one at a time, similar to cards?',
        'options': [
            'CardLayout',
            'GridLayout',
            'FlowLayout',
            'BorderLayout'
        ],
        'answer': 'CardLayout'
    },
    {
        'type': 'mcq',
        'question': 'What keyword is used to define a generic class in Java?',
        'options': [
            'generic',
            'template',
            'class',
            'class ClassName<T>'
        ],
        'answer': 'class ClassName<T>'
    },
    {
        'type': 'mcq',
        'question': 'What is the main difference between Generics and Reflection in Java?',
        'options': [
            'Generics operate at runtime, Reflection at compile time',
            'Generics provide dynamic behavior, Reflection provides type safety',
            'Generics operate at compile time, Reflection at runtime',
            'There is no difference'
        ],
        'answer': 'Generics operate at compile time, Reflection at runtime'
    },
    {
        'type': 'mcq',
        'question': 'How do bounded types in Generics restrict acceptable types?',
        'options': [
            'By specifying a superclass or interface',
            'By allowing any type',
            'By limiting to primitive types',
            'By using wildcards'
        ],
        'answer': 'By specifying a superclass or interface'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is an example of a bounded type in Generics?',
        'options': [
            '<T>',
            '<?>',
            '<T extends Number>',
            '<T super Integer>'
        ],
        'answer': '<T extends Number>'
    },
    {
        'type': 'mcq',
        'question': 'What package in Java provides components for building GUIs like tables and buttons?',
        'options': [
            'java.awt',
            'javax.swing',
            'java.io',
            'java.net'
        ],
        'answer': 'javax.swing'
    },
    {
        'type': 'mcq',
        'question': 'Which layout manager would you use to arrange components in a single row or column?',
        'options': [
            'BoxLayout',
            'FlowLayout',
            'BorderLayout',
            'GridBagLayout'
        ],
        'answer': 'BoxLayout'
    },
    {
        'type': 'mcq',
        'question': 'What is the benefit of using anonymous classes for event listeners in GUIs?',
        'options': [
            'They require less memory',
            'They allow handling multiple actions in one class',
            'They provide a concise way to define event-handling behavior',
            'They improve runtime performance'
        ],
        'answer': 'They provide a concise way to define event-handling behavior'
    },
    {
        'type': 'mcq',
        'question': 'In Generics, what does the \'?\' wildcard allow?',
        'options': [
            'Only one specific type',
            'Multiple types with unknown specifics',
            'Primitive types only',
            'No types'
        ],
        'answer': 'Multiple types with unknown specifics'
    },
    {
        'type': 'mcq',
        'question': 'Which method is used to set a BorderLayout in a JFrame?',
        'options': [
            'setLayout(new FlowLayout())',
            'setLayout(new BorderLayout())',
            'setLayout(new GridLayout())',
            'setLayout(new BoxLayout())'
        ],
        'answer': 'setLayout(new BorderLayout())'
    },
    {
        'type': 'mcq',
        'question': 'What does the GridBagConstraints class help with in GridBagLayout?',
        'options': [
            'Defining row and column sizes',
            'Specifying component constraints',
            'Managing event listeners',
            'Creating new components'
        ],
        'answer': 'Specifying component constraints'
    },
    {
        'type': 'mcq',
        'question': 'How do Generics eliminate the need for manual casting?',
        'options': [
            'By using wildcard types',
            'By ensuring type safety at compile time',
            'By allowing runtime type checks',
            'By supporting multiple inheritance'
        ],
        'answer': 'By ensuring type safety at compile time'
    },
    {
        'type': 'mcq',
        'question': 'Which Swing component would you use to add a clickable button to a GUI?',
        'options': [
            'JLabel',
            'JButton',
            'JTextField',
            'JPanel'
        ],
        'answer': 'JButton'
    },
    {
        'type': 'mcq',
        'question': 'What is the purpose of the ActionListener interface in Java Swing?',
        'options': [
            'To create new GUI components',
            'To handle action events like button clicks',
            'To manage layout managers',
            'To perform background tasks'
        ],
        'answer': 'To handle action events like button clicks'
    },
    {
        'type': 'mcq',
        'question': 'Which layout manager places every element in the same row?',
        'options': [
            'FlowLayout',
            'BoxLayout',
            'GridLayout',
            'BorderLayout'
        ],
        'answer': 'FlowLayout'
    },
    {
        'type': 'mcq',
        'question': 'What does the \'extends\' keyword signify in bounded types?',
        'options': [
            'Inheritance from a superclass',
            'Implementation of an interface',
            'Both inheritance and interface implementation',
            'None of the above'
        ],
        'answer': 'Both inheritance and interface implementation'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following best describes Generic interfaces?',
        'options': [
            'Interfaces that work with a single data type',
            'Interfaces that work with different data types without separate code',
            'Interfaces that use reflection',
            'Interfaces that cannot use Generics'
        ],
        'answer': 'Interfaces that work with different data types without separate code'
    },
    {
        'type': 'mcq',
        'question': 'In Java Swing, which layout manager would you use for a login form with labels and text fields aligned?',
        'options': [
            'FlowLayout',
            'GridLayout',
            'BorderLayout',
            'CardLayout'
        ],
        'answer': 'GridLayout'
    },
    {
        'type': 'mcq',
        'question': 'What does the method \'add\' do in the context of GridBagLayout?',
        'options': [
            'Adds a new row to the grid',
            'Adds a component with specific constraints',
            'Adds a new column to the grid',
            'Adds event listeners to components'
        ],
        'answer': 'Adds a component with specific constraints'
    },
    {
        'type': 'mcq',
        'question': 'How does Generics improve code reusability?',
        'options': [
            'By allowing methods to accept any number of parameters',
            'By enabling classes and methods to operate on specified data types',
            'By reducing the size of the codebase',
            'By simplifying control structures'
        ],
        'answer': 'By enabling classes and methods to operate on specified data types'
    },
    {
        'type': 'mcq',
        'question': 'Which Swing package provides event handling mechanisms?',
        'options': [
            'java.awt.event',
            'javax.swing.event',
            'java.io',
            'javax.net'
        ],
        'answer': 'javax.swing.event'
    },
    {
        'type': 'mcq',
        'question': 'What is the benefit of using CardLayout in a GUI application?',
        'options': [
            'It simplifies the layout to a single row',
            'It allows switching between different panels',
            'It automatically resizes components',
            'It manages event listeners efficiently'
        ],
        'answer': 'It allows switching between different panels'
    },
    {
        'type': 'mcq',
        'question': 'In Generics, what ensures type safety at compile time?',
        'options': [
            'Using raw types',
            'Using wildcards',
        'Specifying type parameters',
            'Using reflection'
        ],
        'answer': 'Specifying type parameters'
    },
    {
        'type': 'mcq',
        'question': 'What is the time complexity of binary search?',
        'options': [
            'O(n)',
            'O(n log n)',
            'O(log n)',
            'O(1)'
        ],
        'answer': 'O(log n)'
    },
    {
        'type': 'mcq',
        'question': 'Which search algorithm has a time complexity of O(n)?',
        'options': [
            'Binary Search',
            'Linear Search',
            'Merge Sort',
            'Heap Sort'
        ],
        'answer': 'Linear Search'
    },
    {
        'type': 'mcq',
        'question': 'What is the time complexity of Selection Sort?',
        'options': [
            'O(n)',
            'O(n^2)',
            'O(n log n)',
            'O(log n)'
        ],
        'answer': 'O(n^2)'
    },
    {
        'type': 'mcq',
        'question': 'Which sorting algorithm divides the array into subarrays, sorts them, and then merges them?',
        'options': [
            'Quick Sort',
            'Merge Sort',
            'Heap Sort',
            'Bubble Sort'
        ],
        'answer': 'Merge Sort'
    },
    {
        'type': 'mcq',
        'question': 'What is the primary characteristic of Heap Sort\'s time complexity?',
        'options': [
            'O(n)',
            'O(n^2)',
            'O(n log n)',
            'O(log n)'
        ],
        'answer': 'O(n log n)'
    },
    {
        'type': 'mcq',
        'question': 'Which data type in Java is a 64-bit integer?',
        'options': [
            'int',
            'long',
            'short',
            'byte'
        ],
        'answer': 'long'
    },
    {
        'type': 'mcq',
        'question': 'What is the default value of a boolean array in Java?',
        'options': [
            'true',
            'false',
            '0',
            'null'
        ],
        'answer': 'false'
    },
    {
        'type': 'mcq',
        'question': 'How do you define an array of integers in Java?',
        'options': [
            'int array;',
            'int[] array;',
            'array int[];',
            'integer array[];'
        ],
        'answer': 'int[] array;'
    },
    {
        'type': 'mcq',
        'question': 'Which method is used to retrieve the length of an array in Java?',
        'options': [
            'length()',
            'size()',
            'getLength()',
            'array.length'
        ],
        'answer': 'array.length'
    },
    {
        'type': 'mcq',
        'question': 'What is the purpose of the ArrayList class in Java?',
        'options': [
            'To create fixed-size arrays',
            'To provide dynamic array functionality',
            'To perform mathematical operations',
            'To handle file I/O'
        ],
        'answer': 'To provide dynamic array functionality'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is an immutable object in Java?',
        'options': [
            'StringBuilder',
            'String',
            'ArrayList',
            'HashMap'
        ],
        'answer': 'String'
    },
    {
        'type': 'mcq',
        'question': 'What does the `charAt` method do in Java strings?',
        'options': [
            'Returns the length of the string',
            'Extracts a substring',
            'Returns the character at a specific index',
            'Converts the string to uppercase'
        ],
        'answer': 'Returns the character at a specific index'
    },
    {
        'type': 'mcq',
        'question': 'Which escape sequence represents a newline in Java?',
        'options': [
            '\\t',
            '\\n',
            '\\b',
            '\\r'
        ],
        'answer': '\\n'
    },
    {
        'type': 'mcq',
        'question': 'What is the time complexity of accessing an element in an ArrayList by index?',
        'options': [
            'O(n)',
            'O(n log n)',
            'O(1)',
            'O(log n)'
        ],
        'answer': 'O(1)'
    },
    {
        'type': 'mcq',
        'question': 'Why should parallel arrays be avoided when possible?',
        'options': [
            'They consume more memory',
            'They make code less readable and harder to maintain',
            'They are slower to access',
            'They cannot store different data types'
        ],
        'answer': 'They make code less readable and harder to maintain'
    }
]