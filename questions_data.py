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
        'answer': 'B',
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
        "type": "mcq",
        "question": "What will be the output of the following code snippet?\n\n```java\nimport java.util.Arrays;\nimport java.util.List;\n\npublic class Test {\n    public static void main(String[] args) {\n        List<? extends Number> numbers = Arrays.asList(1, 2.5, 3);\n        double sum = 0;\n        for (Number num : numbers) {\n            sum += num.doubleValue();\n        }\n        System.out.println(sum);\n    }\n}\n```",
        "options": [
            "6.5",
            "6.0",
            "Compilation error",
            "Runtime error",
            "None of the above"
        ],
        "answer": "A",
        "explanation": "The list contains numbers of type `Integer` and `Double`. The sum is 1.0 + 2.5 + 3.0 = 6.5."
    },
    {
        "type": "mcq",
        "question": "Consider the following code snippet. What will be the output?\n\n```java\nimport java.util.*;\n\npublic class Test {\n    public static void main(String[] args) {\n        Set<Integer> set = new HashSet<>();\n        set.add(1);\n        set.add(2);\n        set.add(1);\n        set.add(3);\n        System.out.println(set.size());\n    }\n}\n```",
        "options": [
            "4",
            "3",
            "2",
            "Compilation error",
            "Runtime error"
        ],
        "answer": "B",
        "explanation": "Sets do not allow duplicate elements. Adding `1` twice does not increase the size. The set contains {1, 2, 3}, so the size is 3."
    },
    {
        "type": "mcq",
        "question": "What will be the result of attempting to compile and run the following code?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        String s1 = \"hello\";\n        String s2 = \"he\" + \"llo\";\n        System.out.println(s1 == s2);\n    }\n}\n```",
        "options": [
            "true",
            "false",
            "Compilation error",
            "Runtime error",
            "Cannot be determined"
        ],
        "answer": "A",
        "explanation": "String literals and compile-time constants are interned in Java. Therefore, `s1` and `s2` refer to the same object, so `s1 == s2` evaluates to `true`."
    },
    {
        "type": "mcq",
        "question": "What is the output of the following code?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        Integer a = 127;\n        Integer b = 127;\n        System.out.println(a == b);\n        Integer c = 128;\n        Integer d = 128;\n        System.out.println(c == d);\n    }\n}\n```",
        "options": [
            "true\ntrue",
            "true\nfalse",
            "false\nfalse",
            "Compilation error",
            "Cannot be determined"
        ],
        "answer": "B",
        "explanation": "Integer values between -128 and 127 are cached. Therefore, `a == b` is `true`. Values outside this range are not cached, so `c == d` is `false`."
    },
    {
        "type": "mcq",
        "question": "Given the following code, what will be the output?\n\n```java\nimport java.util.Arrays;\nimport java.util.Comparator;\n\npublic class Test {\n    public static void main(String[] args) {\n        String[] arr = {\"apple\", \"banana\", \"cherry\"};\n        Arrays.sort(arr, Comparator.comparing(String::length).reversed());\n        System.out.println(Arrays.toString(arr));\n    }\n}\n```",
        "options": [
            "[apple, banana, cherry]",
            "[cherry, banana, apple]",
            "[banana, cherry, apple]",
            "[cherry, apple, banana]",
            "None of the above"
        ],
        "answer": "C",
        "explanation": "The strings are sorted by length in reverse order. \"banana\" and \"cherry\" have length 6, \"apple\" has length 5. The sorted array is [\"banana\", \"cherry\", \"apple\"]."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code snippet?\n\n```java\nimport java.util.Arrays;\nimport java.util.List;\nimport java.util.stream.Collectors;\n\npublic class Test {\n    public static void main(String[] args) {\n        List<String> words = Arrays.asList(\"Java\", \"Stream\", \"API\");\n        String result = words.stream()\n            .collect(Collectors.joining(\"-\"));\n        System.out.println(result);\n    }\n}\n```",
        "options": [
            "Java-Stream-API",
            "Java Stream API",
            "[Java, Stream, API]",
            "Compilation error",
            "None of the above"
        ],
        "answer": "A",
        "explanation": "The `Collectors.joining(\"-\")` method concatenates the stream elements using a hyphen as the delimiter."
    },
    {
        "type": "mcq",
        "question": "Given the following code, what will be the output?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        String str = \"ABCDE\";\n        System.out.println(str.substring(1, 3));\n    }\n}\n```",
        "options": [
            "\"AB\"",
            "\"ABC\"",
            "\"BC\"",
            "\"BCD\"",
            "\"CD\""
        ],
        "answer": "C",
        "explanation": "`substring(1, 3)` returns the substring from index 1 (inclusive) to index 3 (exclusive), which is \"B\" and \"C\", resulting in \"BC\"."
    },
    {
        "type": "mcq",
        "question": "What will be the result of compiling and running the following code?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        String s = null;\n        if (s instanceof String) {\n            System.out.println(\"s is instance of String\");\n        } else {\n            System.out.println(\"s is not instance of String\");\n        }\n    }\n}\n```",
        "options": [
            "\"s is instance of String\"",
            "\"s is not instance of String\"",
            "Compilation error",
            "Runtime NullPointerException",
            "None of the above"
        ],
        "answer": "B",
        "explanation": "When `s` is `null`, `s instanceof String` returns `false`. Therefore, the output is \"s is not instance of String\"."
    },
    {
        "type": "mcq",
        "question": "Consider the following code. What will be the output?\n\n```java\nclass Base {\n    public static void display() {\n        System.out.println(\"Base\");\n    }\n}\n\nclass Derived extends Base {\n    public static void display() {\n        System.out.println(\"Derived\");\n    }\n}\n\npublic class Test {\n    public static void main(String[] args) {\n        Base obj = new Derived();\n        obj.display();\n    }\n}\n```",
        "options": [
            "\"Base\"",
            "\"Derived\"",
            "Compilation error",
            "Runtime error",
            "None of the above"
        ],
        "answer": "A",
        "explanation": "Static methods are not overridden but hidden. The method called depends on the reference type. Since `obj` is of type `Base`, `Base.display()` is called."
    },
    {
        "type": "mcq",
        "question": "What is the output of the following code snippet?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        int[] arr = new int[0];\n        System.out.println(arr.length);\n    }\n}\n```",
        "options": [
            "0",
            "1",
            "Compilation error",
            "Runtime error",
            "None of the above"
        ],
        "answer": "A",
        "explanation": "An array of length zero is valid in Java. The length is `0`."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        String s1 = new String(\"hello\");\n        String s2 = new String(\"hello\");\n        System.out.println(s1 == s2);\n        System.out.println(s1.equals(s2));\n    }\n}\n```",
        "options": [
            "true\ntrue",
            "false\ntrue",
            "true\nfalse",
            "false\nfalse",
            "Compilation error"
        ],
        "answer": "B",
        "explanation": "`s1` and `s2` are different objects, so `s1 == s2` is `false`. The `equals()` method compares the content, so `s1.equals(s2)` is `true`."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code?\n\n```java\nimport java.util.ArrayList;\nimport java.util.List;\n\npublic class Test {\n    public static void main(String[] args) {\n        List<String> list = new ArrayList<>(10);\n        list.add(\"A\");\n        list.add(\"B\");\n        list.add(\"C\");\n        list.remove(1);\n        System.out.println(list);\n    }\n}\n```",
        "options": [
            "[A, B, C]",
            "[A, C]",
            "[A, B]",
            "[B, C]",
            "Compilation error"
        ],
        "answer": "B",
        "explanation": "`list.remove(1);` removes the element at index 1 (\"B\"). The resulting list is [\"A\", \"C\"]."
    },
    {
        "type": "mcq",
        "question": "Which of the following statements about the Java memory model is correct?",
        "options": [
            "Local variables are stored on the heap.",
            "Instance variables are stored on the stack.",
            "Static variables are stored in the method area.",
            "Object references are stored in the code segment.",
            "None of the above."
        ],
        "answer": "C",
        "explanation": "Static variables are stored in the method area of the JVM, which is part of the heap."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code snippet?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        int x = 5;\n        int y = x++ + ++x;\n        System.out.println(\"x = \" + x + \", y = \" + y);\n    }\n}\n```",
        "options": [
            "x = 6, y = 11",
            "x = 7, y = 12",
            "x = 6, y = 10",
            "x = 7, y = 11",
            "x = 8, y = 13"
        ],
        "answer": "B",
        "explanation": "After execution, `x` becomes 7. Calculation: `y = 5 + 7 = 12`. So, `x = 7`, `y = 12`."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        int result = method(5);\n        System.out.println(result);\n    }\n\n    public static int method(int n) {\n        if (n <= 1) return 1;\n        else return n * method(n - 1);\n    }\n}\n```",
        "options": [
            "5",
            "15",
            "120",
            "25",
            "Compilation error"
        ],
        "answer": "C",
        "explanation": "The method calculates the factorial of `n`. `method(5)` returns `5 * 4 * 3 * 2 * 1 = 120`."
    },
    {
        "type": "mcq",
        "question": "Which of the following is true about Java interfaces?",
        "options": [
            "Interfaces can contain implemented methods.",
            "Interfaces cannot contain fields.",
            "Interfaces can extend multiple interfaces.",
            "A class can implement only one interface.",
            "Interfaces can be instantiated directly."
        ],
        "answer": "C",
        "explanation": "Interfaces can extend multiple interfaces. Starting from Java 8, interfaces can also contain default methods (implemented methods)."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code snippet?\n\n```java\nimport java.util.concurrent.atomic.AtomicInteger;\n\npublic class Test {\n    public static void main(String[] args) {\n        AtomicInteger ai = new AtomicInteger(0);\n        ai.getAndIncrement();\n        System.out.println(ai);\n    }\n}\n```",
        "options": [
            "0",
            "1",
            "Compilation error",
            "Runtime error",
            "Cannot be determined"
        ],
        "answer": "B",
        "explanation": "`getAndIncrement()` increments the value after returning the current value. Therefore, `ai` becomes `1`, and `System.out.println(ai);` prints `1`."
    },
    {
        "type": "mcq",
        "question": "What is the difference between `yield()` and `sleep()` methods in Java threads?",
        "options": [
            "`yield()` releases the lock, `sleep()` does not.",
            "`yield()` pauses the thread for a specified time, `sleep()` pauses until another thread notifies.",
            "`yield()` suggests the thread scheduler to give other threads of equal priority a chance, `sleep()` pauses the thread for a specified time.",
            "Both methods do the same.",
            "None of the above."
        ],
        "answer": "C",
        "explanation": "`yield()` is a hint to the scheduler that the thread is willing to yield its current use of a processor. `sleep()` causes the thread to pause for a specified duration."
    },
    {
        "type": "mcq",
        "question": "Given the following code, what will be the output?\n\n```java\nimport java.util.Arrays;\nimport java.util.List;\nimport java.util.function.Predicate;\n\npublic class Test {\n    public static void main(String[] args) {\n        List<String> list = Arrays.asList(\"apple\", \"banana\", \"cherry\");\n        Predicate<String> p = s -> s.startsWith(\"b\");\n        long count = list.stream().filter(p).count();\n        System.out.println(count);\n    }\n}\n```",
        "options": [
            "0",
            "1",
            "2",
            "3",
            "Compilation error"
        ],
        "answer": "B",
        "explanation": "Only \"banana\" starts with 'b', so the count is `1`."
    },
    {
        "type": "mcq",
        "question": "Which of the following statements about Java Enums is correct?",
        "options": [
            "Enums can have constructors, methods, and fields.",
            "Enums cannot implement interfaces.",
            "Enums can extend other classes.",
            "Enums are a type of interface.",
            "Enums cannot have abstract methods."
        ],
        "answer": "A",
        "explanation": "Java Enums can have constructors, methods, fields, and can implement interfaces but cannot extend classes because they already extend `java.lang.Enum`."
    },
    {
        "type": "mcq",
        "question": "Which of the following statements about Java's garbage collection is true?",
        "options": [
            "You can directly invoke the garbage collector to collect an object.",
            "Objects are eligible for garbage collection when they are no longer reachable.",
            "Garbage collection guarantees that a program will not run out of memory.",
            "Finalize methods are always called before an object is garbage collected.",
            "Garbage collection occurs at predictable intervals."
        ],
        "answer": "B",
        "explanation": "An object becomes eligible for garbage collection when there are no more references to it. The garbage collector cannot be forced to collect specific objects."
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
        'answer': 'B',
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
        "type": "mcq",
        "question": "Which declaration is appropriate for storing the number of centimeters in an inch?",
        "options": [
            "`final double centimetersInInch = 2.54;`",
            "`int centimetersInInch = 2.54;`",
            "`double centimetersInInch = 2.54;`",
            "`final int centimetersInInch = 254;`",
            "`final float centimetersInInch = 2.54f;`"
        ],
        "answer": "A",
        "explanation": "Since the value 2.54 is constant and requires decimal precision, it should be declared as a `final double`."
    },
    {
        "type": "mcq",
        "question": "What is the value of `mystery` after the following statements?\n\n```java\nint mystery = 1;\nmystery = 1 - 2 * mystery;\nmystery = mystery + 1;\n```",
        "options": [
            "-1",
            "0",
            "1",
            "-3",
            "2"
        ],
        "answer": "B",
        "explanation": "`mystery = 1 - 2 * 1 = -1`, then `mystery = -1 + 1 = 0`."
    },
    {
        "type": "mcq",
        "question": "What is the issue in the following code snippet?\n\n```java\nint mystery = 1;\nmystery = mystery + 1;\nint mystery = 1 - 2 * mystery;\n```",
        "options": [
            "The variable `mystery` cannot be reassigned.",
            "You cannot declare `mystery` twice in the same scope.",
            "The variable `mystery` must be declared final.",
            "The arithmetic operation `1 - 2 * mystery` is invalid.",
            "There is no issue."
        ],
        "answer": "B",
        "explanation": "A variable cannot be declared twice in the same scope."
    },
    {
        "type": "mcq",
        "question": "What is the value of the following expression?\n\n```java\ndouble x = 2.5;\ndouble y = -1.5;\nint m = 18;\nint n = 4;\nx + n * y - (x + n) * y;\n```",
        "options": [
            "30.5",
            "25.5",
            "6.25",
            "6",
            "None of the above"
        ],
        "answer": "C",
        "explanation": "The expression evaluates as `2.5 + 4 * -1.5 - (2.5 + 4) * -1.5 = 6.25`."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following pseudocode?\n\n```\nDeclare a string names = \"SunMonTueWedThuFriSat\";\nDayNumber = 4;\nStartingPosition = 3 * DayNumber;\nSubstring = names.Substring(StartingPosition, 3);\nPrint Substring;\n```",
        "options": [
            "Sun",
            "Wed",
            "Thu",
            "Fri",
            "Sat"
        ],
        "answer": "C",
        "explanation": "The starting position for day 4 (Thursday) is 3 * 4 = 12. The substring starting at position 12 with length 3 is \"Thu\"."
    },
    {
        "type": "mcq",
        "question": "Which of the following best explains why `System.out.println(20.00 - 19.93);` outputs `0.07000000000000028`?",
        "options": [
            "Floating-point numbers have a limited precision and can introduce rounding errors.",
            "Java does not support exact arithmetic.",
            "The subtraction operation is invalid for floating-point numbers.",
            "The `println` method is not accurate for displaying double values.",
            "None of the above."
        ],
        "answer": "A",
        "explanation": "Floating-point arithmetic in Java is subject to rounding errors due to its limited precision."
    },
    {
        "type": "mcq",
        "question": "What is the value of the following expression if `n = 17` and `m = 18`?\n\n```java\n(int) Math.round(0.5 * (m + n));\n```",
        "options": [
            "17",
            "18",
            "35",
            "36",
            "None of the above"
        ],
        "answer": "B",
        "explanation": "The expression computes `(m + n) * 0.5 = 17.5`. Rounding gives 18."
    },
    {
        "type": "mcq",
        "question": "What is the output of the following string operations?\n\n```java\nString s = \"Hello\";\nString t = \"World\";\nSystem.out.println(s.substring(1, 2) + t.substring(3, 4));\n```",
        "options": [
            "\"el\"",
            "\"ll\"",
            "\"elr\"",
            "\"eo\"",
            "\"et\""
        ],
        "answer": "D",
        "explanation": "The substring of `s` from 1 to 2 is \"e\". The substring of `t` from 3 to 4 is \"o\". Concatenation results in \"eo\"."
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
        'answer': 'B',
        'explanation': 'A layout manager in GUI development is responsible for arranging and managing the placement of components (like buttons, text fields, etc.) within a container such as a window or panel.'
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
        'answer': 'C',
        'explanation': 'GridLayout places components in a grid of cells, each the same size.'
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
        'answer': 'D',
        'explanation': 'GridBagLayout offers complex layouts with components of varying sizes and positions.'
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
        'answer': 'B',
        'explanation': 'The wildcard \'?\' represents an unknown type in generics, allowing for flexibility.'
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
        'answer': 'B',
        'explanation': 'Generics enforce type constraints at compile time, reducing runtime type errors.'
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
        'answer': 'B',
        'explanation': 'Layout managers are responsible for arranging GUI components within a container.'
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
        'answer': 'B',  # Use the option letter corresponding to 'JButton'
        'explanation': 'JButton is the Swing component used to create clickable buttons in GUIs.'
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
        'answer': 'C',
        'explanation': 'An event listener responds to events by executing specific actions when an event occurs.'
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
        'answer': 'A',
        'explanation': 'CardLayout manages multiple components, allowing one to be visible at a time, similar to a deck of cards.'
    },
    {
        'type': 'mcq',
        'question': 'What keyword is used to define a generic class in Java?',
        'options': [
            '`generic`',
            '`template`',
            '`class`',
            '`class ClassName<T>`'
        ],
        'answer': 'D',
        'explanation': 'Generics in Java are defined by specifying type parameters in angle brackets after the class name, such as `class ClassName<T>`.'
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
        'answer': 'A',
        'explanation': 'Bounded types use the `extends` keyword to restrict type parameters to specific superclasses or interfaces.'
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
        'answer': 'B',
        'explanation': 'In Java, the `long` data type is a 64-bit two\'s complement integer.'
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
        'answer': 'C',
        'explanation': 'Generics provide type safety at compile time, while Reflection allows inspection and manipulation of code at runtime.'
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
        'answer': 'B',
        'explanation': 'The `\\n` escape sequence represents a newline character.'
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
        'answer': 'A',
        'explanation': 'Bounded types use the `extends` keyword to specify that type parameters must be subclasses of a particular class or implement a specific interface.'
    },
    {
        'type': 'mcq',
        'question': 'What keyword is used to define a generic class in Java?',
        'options': [
            '`generic`',
            '`template`',
            '`class`',
            '`class ClassName<T>`'
        ],
        'answer': 'D',
        'explanation': 'Generics in Java are defined by specifying type parameters in angle brackets after the class name, like `class ClassName<T>`.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is an example of a bounded type in Generics?',
        'options': [
            '`<T>`',
            '`<?>`',
            '`<T extends Number>`',
            '`<T super Integer>`'
        ],
        'answer': 'C',
        'explanation': '`<T extends Number>` is a bounded type where `T` can be any type that extends `Number`.'
    },
    {
        'type': 'mcq',
        'question': 'What package in Java provides components for building GUIs like tables and buttons?',
        'options': [
            '`java.awt`',
            '`javax.swing`',
            '`java.io`',
            '`java.net`'
        ],
        'answer': 'B',
        'explanation': '`javax.swing` provides a set of "lightweight" components that work the same on all platforms.'
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
        'answer': 'A',
        'explanation': 'BoxLayout places components either on top of each other or in a row.'
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
        'answer': 'C',
        'explanation': 'Anonymous classes let you declare and instantiate a class at the same time, providing a quick way to implement event listeners.'
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
        'answer': 'B',
        'explanation': 'The wildcard `?` represents an unknown type and allows for flexibility when the exact type is not important.'
    },
    {
        'type': 'mcq',
        'question': 'Which method is used to set a BorderLayout in a JFrame?',
        'options': [
            '`setLayout(new FlowLayout())`',
            '`setLayout(new BorderLayout())`',
            '`setLayout(new GridLayout())`',
            '`setLayout(new BoxLayout())`'
        ],
        'answer': 'B',
        'explanation': 'You set the layout manager of a container by calling `setLayout(new BorderLayout())`.'
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
        'answer': 'B',
        'explanation': '`GridBagConstraints` specify constraints for components that are laid out using `GridBagLayout`, such as grid position and size.'
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
        'answer': 'B',
        'explanation': 'Generics enforce type constraints at compile time, removing the need for manual casting and reducing the risk of runtime errors.'
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
        'answer': 'B',
        'explanation': 'The `ActionListener` interface is used to handle action events, such as button clicks, by implementing the `actionPerformed` method.'
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
        'answer': 'A',
        'explanation': 'The `FlowLayout` manager arranges components in a row, wrapping them to the next line if the row exceeds the container\'s width.'
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
        'answer': 'C',
        'explanation': 'The `extends` keyword in bounded types signifies that the type parameter can be a subclass or implement an interface, combining inheritance and interface implementation.'
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
        'answer': 'B',
        'explanation': 'Generic interfaces allow the same interface to work with multiple data types without requiring separate implementations for each type.'
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
        'answer': 'B',
        'explanation': 'The `GridLayout` manager arranges components in a grid of rows and columns, making it suitable for aligning labels and text fields in a form.'
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
        'answer': 'B',
        'explanation': 'In GridBagLayout, the `add` method places a component using GridBagConstraints.'
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
        'answer': 'B',
        'explanation': 'Generics enable classes and methods to operate on specified data types, allowing the same code to work with different types while ensuring type safety.'
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
        'answer': 'B',
        'explanation': 'The `javax.swing.event` package provides classes and interfaces for event handling mechanisms in Swing-based GUIs.'
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
        'answer': 'B',
        'explanation': 'The `CardLayout` manager allows for switching between multiple panels, making it ideal for creating wizard-style interfaces or tabbed panels.'
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
        'answer': 'C',
        'explanation': 'Specifying type parameters ensures type safety at compile time by restricting the types that can be used with a generic class or method.'
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
        'answer': 'C',
        'explanation': 'Binary search divides the search space in half at each step, resulting in a time complexity of O(log n).'
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
        'answer': 'B',
        'explanation': 'Linear search has a time complexity of O(n) because it checks each element in the array one by one until the target is found or the array ends.'
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
        'answer': 'B',
        'explanation': 'Selection Sort has a time complexity of O(n^2) because it involves nested loops: one to iterate through the elements and another to find the minimum element in the remaining list.'
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
        'answer': 'B',
        'explanation': 'Merge Sort divides the array into smaller subarrays, sorts them recursively, and then merges the sorted subarrays to produce the final sorted array.'
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
        'answer': 'C',
        'explanation': 'Heap Sort has a time complexity of O(n log n) due to the heap operations.'
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
        'answer': 'B',
        'explanation': 'Boolean array elements default to `false` in Java.'
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
        'answer': 'B',
        'explanation': 'In Java, arrays are declared with the type followed by square brackets, such as `int[] array`.'
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
        'answer': 'D',
        'explanation': 'The `length` property (not a method) is used to get the size of an array in Java, accessed as `array.length`.'
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
        'answer': 'B',
        'explanation': 'The `ArrayList` class provides dynamic arrays that can grow or shrink in size as needed.'
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
        'answer': 'B',
        'explanation': 'Strings in Java are immutable, meaning their values cannot be changed after they are created.'
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
        'answer': 'C',
        'explanation': 'The `charAt` method returns the character at the specified index in a string.'
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
        'answer': 'C',
        'explanation': 'Accessing an element by index in an ArrayList is O(1) due to direct indexing.'
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
        'answer': 'B',
        'explanation': 'Parallel arrays can lead to code that is hard to read and maintain due to the need to keep multiple arrays in sync.'
    },
    {
        'type': 'mcq',
        'question': 'What will be the output of the following code snippet?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        int a = 5;\n        int b = 2;\n        double c = a / b;\n        System.out.println(c);\n    }\n}\n```',
        'options': ['2', '2.5', '2.0', 'Compilation error', 'Runtime error'],
        'answer': 'C',
        'explanation': 'Integer division results in truncation, so the result is 2.0 when implicitly cast to double.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following will cause a compilation error in Java?\n\n```java\nclass Test {\n    public void method(final int x) {\n        x = x + 1;\n    }\n}\n```',
        'options': [
            'The method modifies a final parameter.',
            'Final parameters cannot be passed to methods.',
            'The code will compile successfully.',
            'Final variables must be initialized immediately.',
            'Final variables cannot be modified after initialization.'
        ],
        'answer': 'A',
        'explanation': 'Final parameters cannot be reassigned, and attempting to do so will result in a compilation error.'
    },
    {
        'type': 'mcq',
        'question': 'What will be the output of the following code snippet?\n\n```java\nclass Test {\n    public static void main(String[] args) {\n        String s1 = new String("hello");\n        String s2 = "hello";\n        System.out.println(s1 == s2);\n    }\n}\n```',
        'options': ['true', 'false', 'Compilation error', 'Runtime error', 'Cannot be determined'],
        'answer': 'B',
        'explanation': '`s1` and `s2` refer to different objects; `==` compares references, not values.'
    },
    {
        'type': 'mcq',
        'question': 'Given the following code, which statement about the output is correct?\n\n```java\nimport java.util.*;\n\npublic class Test {\n    public static void main(String[] args) {\n        List<String> list = new ArrayList<>();\n        list.add("one");\n        list.add("two");\n        list.remove(1);\n        System.out.println(list.get(1));\n    }\n}\n```',
        'options': ['one', 'two', 'Compilation error', 'IndexOutOfBoundsException', 'Runtime error'],
        'answer': 'D',
        'explanation': 'Removing the element at index 1 leaves the list with only one element. Accessing index 1 causes an `IndexOutOfBoundsException`.'
    },
    {
        'type': 'mcq',
        'question': 'What is the output of the following code snippet?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        int[] array = {1, 2, 3};\n        System.out.println(array[3]);\n    }\n}\n```',
        'options': ['1', '2', '3', 'Compilation error', 'ArrayIndexOutOfBoundsException'],
        'answer': 'E',
        'explanation': 'Accessing an out-of-bounds index throws an `ArrayIndexOutOfBoundsException`.'
    },
    {
        'type': 'mcq',
        'question': 'What will happen if the following code is executed?\n\n```java\nclass Test {\n    public static void main(String[] args) {\n        int result = divide(10, 0);\n    }\n\n    public static int divide(int a, int b) {\n        return a / b;\n    }\n}\n```',
        'options': [
            'The program will print "Infinity".',
            'The program will throw an ArithmeticException.',
            'The program will compile but crash at runtime.',
            'The program will output 0.',
            'The program will not compile.'
        ],
        'answer': 'B',
        'explanation': 'Division by zero with integers results in an `ArithmeticException`.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following is NOT true about the `equals()` method in Java?',
        'options': [
            'It is defined in the `Object` class.',
            'It compares two objects for reference equality by default.',
            'It can be overridden in user-defined classes.',
            'It is always symmetric, transitive, and reflexive.',
            'It is used for comparing primitive data types.'
        ],
        'answer': 'E',
        'explanation': '`equals()` is used to compare objects, not primitives. Primitives use `==`.'
    },
    {
        'type': 'mcq',
        'question': 'What will be the output of the following code snippet?\n\n```java\nclass Test {\n    public static void main(String[] args) {\n        System.out.println(10 + "20" + 30);\n    }\n}\n```',
        'options': ['60', '102030', '10 20 30', '1030', 'Compilation error'],
        'answer': 'B',
        'explanation': 'String concatenation occurs: "10" + "20" = "1020", and "1020" + 30 = "102030".'
    },
    {
        'type': 'mcq',
        'question': 'What will be the output of the following code snippet?\n\n```java\nclass Test {\n    public static void main(String[] args) {\n        try {\n            int[] arr = {1, 2, 3};\n            System.out.println(arr[5]);\n        } catch (ArrayIndexOutOfBoundsException e) {\n            System.out.println("Caught exception");\n        } finally {\n            System.out.println("Finally block executed");\n        }\n    }\n}\n```',
        'options': [
            'Caught exception\nFinally block executed',
            'Finally block executed',
            'Caught exception',
            'Runtime error',
            'Compilation error'
        ],
        'answer': 'A',
        'explanation': 'The `catch` block handles the exception, and the `finally` block executes afterward.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following scenarios will result in a deadlock in Java?\n\n```java\nThread 1 locks Object A, then locks Object B.\nThread 2 locks Object B, then locks Object A.\n```',
        'options': [
            'When both threads are started simultaneously.',
            'When one thread sleeps while holding a lock.',
            'When neither thread calls notify().',
            'When both threads attempt to acquire the locks in the opposite order.',
            'When both threads use synchronized blocks.'
        ],
        'answer': 'D',
        'explanation': 'A deadlock occurs when two threads hold locks and wait for each other to release them in reverse order.'
    },
    {
        'type': 'mcq',
        'question': 'What will be the output of the following program?\n\n```java\nclass Test {\n    public static void main(String[] args) {\n        String s1 = "Hello";\n        String s2 = new String("Hello");\n        System.out.println(s1.equals(s2));\n        System.out.println(s1 == s2);\n    }\n}\n```',
        'options': [
            'true\ntrue',
            'true\nfalse',
            'false\nfalse',
            'false\ntrue',
            'Compilation error'
        ],
        'answer': 'B',
        'explanation': '`equals()` compares values and returns true. `==` compares references, which are different here.'
    },
    {
        'type': 'mcq',
        'question': 'What is the result of the following code?\n\n```java\nclass Test {\n    public static void main(String[] args) {\n        Object obj = null;\n        System.out.println(obj instanceof String);\n    }\n}\n```',
        'options': ['true', 'false', 'Compilation error', 'Runtime error', 'Cannot be determined'],
        'answer': 'B',
        'explanation': 'The `instanceof` operator returns false if the object is null.'
    },
    {
        'type': 'mcq',
        'question': 'What is the output of the following code snippet?\n\n```java\nclass Test {\n    public static void main(String[] args) {\n        int x = 0;\n        x += ++x + x++;\n        System.out.println(x);\n    }\n}\n```',
        'options': ['2', '3', '4', '5', 'Compilation error'],
        'answer': 'B',
        'explanation': 'The value of `x` changes during the operation. It evaluates as `x = 0 + 1 + 1`.'
    },
    {
        'type': 'mcq',
        'question': 'What will happen if the following code is executed?\n\n```java\nclass Parent {\n    public void display() {\n        System.out.println("Parent");\n    }\n}\n\nclass Child extends Parent {\n    @Override\n    public void display() {\n        System.out.println("Child");\n    }\n\n    public static void main(String[] args) {\n        Parent obj = new Child();\n        obj.display();\n    }\n}\n```',
        'options': ['Parent', 'Child', 'Compilation error', 'Runtime error', 'Cannot be determined'],
        'answer': 'B',
        'explanation': 'Dynamic method dispatch calls the overridden method in the child class.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following keywords can be used to prevent a class from being subclassed?',
        'options': ['static', 'final', 'abstract', 'synchronized', 'private'],
        'answer': 'B',
        'explanation': 'The `final` keyword prevents a class from being extended.'
    },
    {
        'type': 'mcq',
        'question': 'What will be the output of the following code snippet?\n\n```java\nabstract class Animal {\n    abstract void sound();\n    void breathe() {\n        System.out.println("Breathing...");\n    }\n}\n\nclass Dog extends Animal {\n    void sound() {\n        System.out.println("Woof Woof");\n    }\n}\n\npublic class Test {\n    public static void main(String[] args) {\n        Animal a = new Dog();\n        a.breathe();\n        a.sound();\n    }\n}\n```',
        'options': [
            'Compilation error',
            'Runtime error',
            'Breathing...\nWoof Woof',
            'Breathing...\nNullPointerException',
            'Breathing...\nCompilation error in Dog'
        ],
        'answer': 'C',
        'explanation': 'The `Dog` class correctly implements the abstract `sound` method, and `breathe` is a concrete method inherited from the `Animal` class.'
    },
    {
        'type': 'mcq',
        'question': 'What will happen if you try to compile and run the following code?\n\n```java\ninterface Vehicle {\n    default void start() {\n        System.out.println("Starting vehicle...");\n    }\n}\n\npublic class Test implements Vehicle {\n    public static void main(String[] args) {\n        Vehicle v = new Test();\n        v.start();\n    }\n}\n```',
        'options': [
            'Compilation error due to the default method in the interface.',
            'Runtime error due to unimplemented methods.',
            'Starting vehicle...',
            'Default method overrides are not allowed.',
            'The program will run, but no output will be shown.'
        ],
        'answer': 'C',
        'explanation': 'Since Java 8, interfaces can have default method implementations, and the code executes the `start` method correctly.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following statements about anonymous classes is TRUE?\n\n```java\nRunnable r = new Runnable() {\n    public void run() {\n        System.out.println("Running");\n    }\n};\n```',
        'options': [
            'Anonymous classes can have constructors.',
            'Anonymous classes can be used to override methods on the go.',
            'Anonymous classes must be declared static.',
            'Anonymous classes cannot implement interfaces.',
            'Anonymous classes are compiled to the same `.class` file as their enclosing class.'
        ],
        'answer': 'B',
        'explanation': 'Anonymous classes are often used to override or implement methods quickly without creating a named class.'
    },
    {
        'type': 'mcq',
        'question': 'What will be the output of the following code snippet?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        Integer x = 100;\n        Integer y = 100;\n        System.out.println(x == y);\n\n        Integer a = 200;\n        Integer b = 200;\n        System.out.println(a == b);\n    }\n}\n```',
        'options': ['true\ntrue', 'false\nfalse', 'true\nfalse', 'Compilation error', 'Runtime error'],
        'answer': 'C',
        'explanation': 'Integers between -128 and 127 are cached, so `x` and `y` reference the same object, but `a` and `b` do not.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following correctly demonstrates the Singleton pattern in Java?',
        'options': [
            '```java\npublic class Singleton {\n    private static Singleton instance;\n    private Singleton() {}\n    public static Singleton getInstance() {\n        if (instance == null) instance = new Singleton();\n        return instance;\n    }\n}\n```',
            '```java\npublic class Singleton {\n    public Singleton() {}\n}\n```',
            '```java\npublic class Singleton {\n    private Singleton() {}\n}\n```',
            '```java\npublic class Singleton {\n    public static Singleton getInstance() {\n        return new Singleton();\n    }\n}\n```',
            'None of the above'
        ],
        'answer': 'A',
        'explanation': 'The Singleton pattern ensures only one instance of the class is created and provides a global point of access to it.'
    },
    {
        'type': 'mcq',
        'question': 'Which of the following will cause a compilation error?\n\n```java\ninterface Animal {\n    default void eat() {\n        System.out.println("Eating...");\n    }\n    void sleep();\n}\n\nabstract class Mammal implements Animal {\n    public abstract void walk();\n}\n\nclass Dog extends Mammal {\n    public void walk() {\n        System.out.println("Walking...");\n    }\n}\n```',
        'options': [
            'Dog does not implement sleep().',
            'Mammal cannot implement an interface.',
            'Abstract classes cannot have abstract methods.',
            'Default methods cannot be used in interfaces.',
            'The code will compile and run without errors.'
        ],
        'answer': 'A',
        'explanation': 'The `Dog` class must implement all abstract methods, including `sleep` from the `Animal` interface.'
    },
    {
        'type': 'mcq',
        'question': 'What will be the output of the following code snippet?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        int num = 5;\n        Integer obj = num; // Autoboxing\n        int val = obj;    // Unboxing\n        System.out.println(obj + val);\n    }\n}\n```',
        'options': ['10', 'Compilation error', 'Runtime error', '5', 'Cannot be determined'],
        'answer': 'A',
        'explanation': 'Autoboxing and unboxing work seamlessly, so the result is `5 + 5 = 10`.'
    },
    {
        'type': 'mcq',
        'question': 'What will be the output of the following code snippet?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        List<Integer> list = Arrays.asList(1, 2, 3);\n        list.add(4);\n    }\n}\n```',
        'options': [
            'The list will contain [1, 2, 3, 4].',
            'Compilation error.',
            'Runtime error: UnsupportedOperationException.',
            'The list will not be modified.',
            'Cannot be determined.'
        ],
        'answer': 'C',
        'explanation': 'The `asList` method returns a fixed-size list, and attempting to modify it throws `UnsupportedOperationException`.'
    },
    {
        "type": "mcq",
        "question": "Which of the following correctly demonstrates the use of a LinkedList in Java?\n\n```java\nimport java.util.LinkedList;\npublic class Test {\n    public static void main(String[] args) {\n        LinkedList<Integer> list = new LinkedList<>();\n        list.add(10);\n        list.addFirst(5);\n        list.addLast(15);\n        System.out.println(list.get(1));\n    }\n}\n```",
        "options": ["10", "5", "15", "Compilation error", "Runtime error"],
        "answer": "A",
        "explanation": "The `get(1)` method retrieves the element at index 1, which is 10 after adding 5 to the front and 15 to the back."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code snippet?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        HashSet<String> set = new HashSet<>();\n        set.add(\"Hello\");\n        set.add(\"World\");\n        set.add(\"Hello\");\n        System.out.println(set.size());\n    }\n}\n```",
        "options": ["1", "2", "3", "Compilation error", "Cannot be determined"],
        "answer": "B",
        "explanation": "HashSet does not allow duplicate elements, so only two unique elements are present."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following lambda expression?\n\n```java\nimport java.util.Arrays;\nimport java.util.List;\npublic class Test {\n    public static void main(String[] args) {\n        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);\n        numbers.forEach(num -> System.out.print(num * 2 + \" \"));\n    }\n}\n```",
        "options": ["2 4 6 8 10", "1 2 3 4 5", "Compilation error", "Runtime error", "Cannot be determined"],
        "answer": "A",
        "explanation": "The lambda expression multiplies each number in the list by 2 and prints the result."
    },
    {
        "type": "mcq",
        "question": "Which of the following will cause a compilation error?\n\n```java\ninterface Animal {\n    default void eat() {\n        System.out.println(\"Eating...\");\n    }\n    void sleep();\n}\n\nabstract class Mammal implements Animal {\n    public abstract void walk();\n}\n\nclass Dog extends Mammal {\n    public void walk() {\n        System.out.println(\"Walking...\");\n    }\n}\n```",
        "options": [
            "Dog does not implement sleep().",
            "Mammal cannot implement an interface.",
            "Abstract classes cannot have abstract methods.",
            "Default methods cannot be used in interfaces.",
            "The code will compile and run without errors."
        ],
        "answer": "A",
        "explanation": "The `Dog` class must implement all abstract methods, including `sleep` from the `Animal` interface."
    },
    {
        "type": "mcq",
        "question": "What will happen if you attempt to compile and run the following code?\n\n```java\npublic class SingletonTest {\n    private static SingletonTest instance;\n    private SingletonTest() {}\n    public static SingletonTest getInstance() {\n        if (instance == null) {\n            instance = new SingletonTest();\n        }\n        return instance;\n    }\n}\n\nclass Test {\n    public static void main(String[] args) {\n        SingletonTest obj1 = SingletonTest.getInstance();\n        SingletonTest obj2 = SingletonTest.getInstance();\n        System.out.println(obj1 == obj2);\n    }\n}\n```",
        "options": ["true", "false", "Compilation error", "Runtime error", "Cannot be determined"],
        "answer": "A",
        "explanation": "The Singleton pattern ensures only one instance of the class exists, so obj1 and obj2 refer to the same instance."
    },
    {
        "type": "mcq",
        "question": "Which of the following correctly demonstrates the use of a bounded type parameter in Java?",
        "options": [
            "```java\npublic <T extends Number> void printNumber(T t) {\n    System.out.println(t);\n}\n```",
            "```java\npublic <T> void printNumber(T t) {\n    System.out.println(t);\n}\n```",
            "```java\npublic <T super Number> void printNumber(T t) {\n    System.out.println(t);\n}\n```",
            "```java\npublic void printNumber(Number t) {\n    System.out.println(t);\n}\n```",
            "None of the above"
        ],
        "answer": "A",
        "explanation": "The `extends` keyword is used to specify a bounded type parameter that must extend `Number` or its subclasses."
    },
    {
        "type": "mcq",
        "question": "What is the output of the following code snippet?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        Optional<String> opt = Optional.ofNullable(null);\n        System.out.println(opt.orElse(\"Default\"));\n    }\n}\n```",
        "options": ["null", "Default", "Compilation error", "Runtime error", "Cannot be determined"],
        "answer": "B",
        "explanation": "The `orElse` method provides a default value when the `Optional` is empty."
    },
    {
        "type": "mcq",
        "question": "What will be the result of running the following code?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        Stack<Integer> stack = new Stack<>();\n        stack.push(10);\n        stack.push(20);\n        stack.pop();\n        System.out.println(stack.peek());\n    }\n}\n```",
        "options": ["10", "20", "Compilation error", "Runtime error", "Cannot be determined"],
        "answer": "A",
        "explanation": "The `pop` method removes the last element added, leaving 10 at the top of the stack."
    },
    {
        "type": "mcq",
        "question": "Which of the following statements about abstract classes is true?",
        "options": [
            "Abstract classes can have constructors.",
            "Abstract classes cannot have concrete methods.",
            "Abstract classes cannot be extended.",
            "Abstract classes are equivalent to interfaces.",
            "None of the above"
        ],
        "answer": "A",
        "explanation": "Abstract classes can have constructors, but they cannot be instantiated directly."
    },
    {
        "type": "mcq",
        "question": "Which statement about autoboxing in Java is correct?",
        "options": [
            "Autoboxing converts a primitive type to its corresponding wrapper type.",
            "Autoboxing converts a wrapper type to its corresponding primitive type.",
            "Autoboxing allows primitive types to be stored in collections without casting.",
            "Autoboxing is the process of casting between unrelated types.",
            "Autoboxing is used only with Strings."
        ],
        "answer": "A",
        "explanation": "Autoboxing automatically converts primitive types to their wrapper types."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code snippet?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        int num = 5;\n        Integer obj = num; // Autoboxing\n        int val = obj;    // Unboxing\n        System.out.println(obj + val);\n    }\n}\n```",
        "options": ["10", "Compilation error", "Runtime error", "5", "Cannot be determined"],
        "answer": "A",
        "explanation": "Autoboxing and unboxing work seamlessly, so the result is `5 + 5 = 10`."
    },
    {
        "type": "mcq",
        "question": "Which of the following is true about the TreeSet class in Java?",
        "options": [
            "TreeSet allows duplicate elements.",
            "TreeSet elements are ordered according to their natural ordering.",
            "TreeSet is not part of the Collections Framework.",
            "TreeSet is faster than HashSet for lookups.",
            "TreeSet does not implement the Set interface."
        ],
        "answer": "B",
        "explanation": "TreeSet maintains elements in their natural ordering or using a comparator if specified."
    },
    {
        "type": "mcq",
        "question": "What will the following lambda expression return?\n\n```java\nimport java.util.Arrays;\nimport java.util.List;\nimport java.util.stream.Collectors;\npublic class Test {\n    public static void main(String[] args) {\n        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);\n        List<Integer> result = numbers.stream().filter(num -> num % 2 == 0).collect(Collectors.toList());\n        System.out.println(result);\n    }\n}\n```",
        "options": [
            "[1, 3, 5]",
            "[2, 4]",
            "[1, 2, 3, 4, 5]",
            "Compilation error",
            "Runtime error"
        ],
        "answer": "B",
        "explanation": "The stream filters out odd numbers, leaving only even numbers `[2, 4]`."
    },
    {
        "type": "mcq",
        "question": "What will happen if you attempt to modify the following `List` created using `Arrays.asList`?\n\n```java\nimport java.util.Arrays;\nimport java.util.List;\npublic class Test {\n    public static void main(String[] args) {\n        List<Integer> list = Arrays.asList(1, 2, 3);\n        list.add(4);\n    }\n}\n```",
        "options": [
            "The list will contain [1, 2, 3, 4].",
            "Compilation error.",
            "Runtime error: UnsupportedOperationException.",
            "The list will not be modified.",
            "Cannot be determined."
        ],
        "answer": "C",
        "explanation": "The `asList` method returns a fixed-size list, and attempting to modify it throws `UnsupportedOperationException`."
    },
    {
        "type": "mcq",
        "question": "What is the purpose of the `synchronized` keyword in Java?",
        "options": [
            "To improve the speed of execution.",
            "To ensure that a method or block of code can only be accessed by one thread at a time.",
            "To make a class immutable.",
            "To prevent compilation errors in multi-threaded programs.",
            "None of the above."
        ],
        "answer": "B",
        "explanation": "The `synchronized` keyword ensures mutual exclusion, allowing only one thread to execute a method or block of code at a time."
    },
    {
        "type": "mcq",
        "question": "Which of the following code snippets demonstrates a Factory design pattern?\n\n```java\nabstract class Animal {\n    public abstract void speak();\n}\nclass Dog extends Animal {\n    public void speak() { System.out.println(\"Woof\"); }\n}\nclass Cat extends Animal {\n    public void speak() { System.out.println(\"Meow\"); }\n}\nclass AnimalFactory {\n    public static Animal createAnimal(String type) {\n        if (type.equals(\"Dog\")) return new Dog();\n        else if (type.equals(\"Cat\")) return new Cat();\n        else throw new IllegalArgumentException(\"Unknown type\");\n    }\n}\n\npublic class Test {\n    public static void main(String[] args) {\n        Animal animal = AnimalFactory.createAnimal(\"Dog\");\n        animal.speak();\n    }\n}\n```",
        "options": [
            "Correct implementation of Factory pattern.",
            "Incorrect: Factory pattern must use interfaces.",
            "Incorrect: Factory pattern must return a singleton.",
            "Incorrect: Factory pattern cannot handle dynamic types.",
            "None of the above."
        ],
        "answer": "A",
        "explanation": "The Factory pattern creates objects without specifying the exact class type, as shown in the `AnimalFactory` class."
    },
    {
        "type": "mcq",
        "question": "What will the following code output?\n\n```java\nimport java.util.HashMap;\npublic class Test {\n    public static void main(String[] args) {\n        HashMap<String, Integer> map = new HashMap<>();\n        map.put(\"One\", 1);\n        map.put(\"Two\", 2);\n        map.put(\"One\", 10);\n        System.out.println(map.get(\"One\"));\n    }\n}\n```",
        "options": ["1", "2", "10", "Compilation error", "Cannot be determined"],
        "answer": "C",
        "explanation": "The `put` method replaces the value for the key `One` with the new value `10`."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code snippet?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        try {\n            int result = 10 / 0;\n        } catch (ArithmeticException e) {\n            System.out.println(\"Arithmetic Exception\");\n        } finally {\n            System.out.println(\"Finally Block\");\n        }\n    }\n}\n```",
        "options": [
            "Arithmetic Exception",
            "Finally Block",
            "Arithmetic Exception\\nFinally Block",
            "Compilation error",
            "Cannot be determined"
        ],
        "answer": "C",
        "explanation": "The `catch` block handles the exception and prints \"Arithmetic Exception\", and the `finally` block executes regardless of exceptions."
    },
    {
        "type": "mcq",
        "question": "What is the primary benefit of using streams in Java?",
        "options": [
            "Simplifies processing collections through declarative code.",
            "Provides faster performance than loops in all cases.",
            "Ensures thread safety.",
            "Automatically handles exceptions in data processing.",
            "None of the above."
        ],
        "answer": "A",
        "explanation": "Streams allow processing collections in a clear and declarative manner with operations like `filter`, `map`, and `collect`."
    },
    {
        "type": "mcq",
        "question": "Which of the following statements about a Queue is correct?",
        "options": [
            "Elements are added at the front and removed from the back.",
            "Elements are added at the back and removed from the front.",
            "Elements are added and removed randomly.",
            "Queue supports direct indexing of elements.",
            "Queue does not allow duplicate elements."
        ],
        "answer": "B",
        "explanation": "A Queue follows the First-In-First-Out (FIFO) principle, where elements are added at the back and removed from the front."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code snippet?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        int value = 105;\n        do {\n            System.out.println(\"Value: \" + value);\n            value -= 5;\n        } while (value >= 100);\n    }\n}\n```",
        "options": [
            "Value: 105",
            "Value: 105\\nValue: 100",
            "No output",
            "Compilation error",
            "Value: 105\\nValue: 100\\nValue: 95"
        ],
        "answer": "B",
        "explanation": "The `do-while` loop executes at least once. It prints `Value: 105`, then decrements `value` to 100, which satisfies the condition `value >= 100`, so it loops again and prints `Value: 100`. After decrementing to 95, the condition fails, and the loop exits."
    },
    {
        "type": "mcq",
        "question": "What exception will be thrown if the following code is executed and the file `input.txt` does not exist?\n\n```java\nimport java.io.File;\nimport java.io.FileNotFoundException;\nimport java.util.Scanner;\npublic class Test {\n    public static void main(String[] args) throws Exception {\n        File inputFile = new File(\"input.txt\");\n        Scanner in = new Scanner(inputFile);\n    }\n}\n```",
        "options": [
            "IOException",
            "FileNotFoundException",
            "NullPointerException",
            "NoSuchElementException",
            "InputMismatchException"
        ],
        "answer": "B",
        "explanation": "If the specified file does not exist, the `Scanner` constructor throws a `FileNotFoundException`."
    },
    {
        "type": "mcq",
        "question": "Given the following code, what will be the output?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        String text = \"Hello123World456\";\n        String result = text.replaceAll(\"[^A-Za-z]+\", \"-\");\n        System.out.println(result);\n    }\n}\n```",
        "options": [
            "Hello-World-",
            "Hello123World456",
            "Hello-World",
            "-Hello-World-",
            "Compilation error"
        ],
        "answer": "A",
        "explanation": "The regex `[^A-Za-z]+` matches any sequence of non-letter characters (the numbers), and replaces them with `-`. So `123` and `456` are replaced with `-`, resulting in `Hello-World-`."
    },
    {
        "type": "mcq",
        "question": "If the following program is executed with the command `java Test -v input.txt`, what will be the output?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        System.out.println(args[0]);\n    }\n}\n```",
        "options": [
            "-v",
            "input.txt",
            "Test",
            "java",
            "ArrayIndexOutOfBoundsException"
        ],
        "answer": "A",
        "explanation": "The `args` array contains `{ \"-v\", \"input.txt\" }`, so `args[0]` is `\"-v\"`."
    },
    {
        "type": "mcq",
        "question": "What will happen when the following code is executed?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        String str = null;\n        if (str.length() == 0) {\n            System.out.println(\"Empty String\");\n        }\n    }\n}\n```",
        "options": [
            "Prints: Empty String",
            "Prints nothing",
            "Throws NullPointerException",
            "Compilation error",
            "Throws IllegalArgumentException"
        ],
        "answer": "C",
        "explanation": "Attempting to call `length()` on a null reference `str` will throw a `NullPointerException`."
    },
    {
        "type": "mcq",
        "question": "What exception will be thrown if the following code is executed and the user inputs a non-integer value?\n\n```java\nimport java.util.Scanner;\npublic class Test {\n    public static void main(String[] args) {\n        Scanner in = new Scanner(System.in);\n        int number = in.nextInt();\n        System.out.println(\"You entered: \" + number);\n    }\n}\n```",
        "options": [
            "InputMismatchException",
            "NumberFormatException",
            "IOException",
            "NoSuchElementException",
            "NullPointerException"
        ],
        "answer": "A",
        "explanation": "The `nextInt()` method throws an `InputMismatchException` if the next token does not match the `Integer` pattern."
    },
    {
        "type": "mcq",
        "question": "Which of the following statements is true regarding the visibility and size of a `JFrame` in Java Swing?",
        "options": [
            "A `JFrame` is visible by default when created.",
            "You must call `setVisible(true)` to display the `JFrame`.",
            "Calling `setSize()` is optional as the frame will auto-resize.",
            "Calling `setTitle()` makes the `JFrame` visible.",
            "You cannot change the size of a `JFrame` once it's created."
        ],
        "answer": "B",
        "explanation": "A `JFrame` is not visible by default. You must call `setVisible(true)` to display it."
    },
    {
        "type": "mcq",
        "question": "In implementing an `ActionListener`, which method must be overridden to handle button click events?",
        "options": [
            "mouseClicked(MouseEvent e)",
            "keyPressed(KeyEvent e)",
            "actionPerformed(ActionEvent e)",
            "itemStateChanged(ItemEvent e)",
            "valueChanged(ListSelectionEvent e)"
        ],
        "answer": "C",
        "explanation": "The `ActionListener` interface requires the `actionPerformed(ActionEvent e)` method to be overridden."
    },
    {
        "type": "mcq",
        "question": "Which method would you use to retrieve the text from a `JTextField` component?",
        "options": [
            "getText()",
            "setText()",
            "appendText()",
            "getValue()",
            "retrieveText()"
        ],
        "answer": "A",
        "explanation": "The `getText()` method returns the text contained in a `JTextField`."
    },
    {
        "type": "mcq",
        "question": "What will the following code draw when placed inside a `paintComponent(Graphics g)` method?\n\n```java\ng.setColor(Color.RED);\ng.fillOval(50, 50, 100, 100);\ng.setColor(Color.BLUE);\ng.drawRect(50, 50, 100, 100);\n```",
        "options": [
            "A red circle with a blue square around it.",
            "A red square with a blue circle around it.",
            "A red circle with a blue square overlapping it.",
            "A red circle with a blue rectangle border around it.",
            "A blue rectangle filled with red color."
        ],
        "answer": "D",
        "explanation": "The code draws a filled red circle and then an unfilled blue rectangle (border) around it."
    },
    {
        "type": "mcq",
        "question": "When implementing the `MouseListener` interface, which method is called when the mouse button is pressed and released without moving the mouse?",
        "options": [
            "mousePressed(MouseEvent e)",
            "mouseReleased(MouseEvent e)",
            "mouseClicked(MouseEvent e)",
            "mouseEntered(MouseEvent e)",
            "mouseExited(MouseEvent e)"
        ],
        "answer": "C",
        "explanation": "The `mouseClicked` method is invoked when a mouse button is pressed and released at the same location."
    },
    {
        "type": "mcq",
        "question": "Which layout manager arranges components in five regions: `NORTH`, `SOUTH`, `EAST`, `WEST`, and `CENTER`?",
        "options": [
            "FlowLayout",
            "GridLayout",
            "BorderLayout",
            "BoxLayout",
            "CardLayout"
        ],
        "answer": "C",
        "explanation": "`BorderLayout` divides the container into five areas: `NORTH`, `SOUTH`, `EAST`, `WEST`, and `CENTER`."
    },
    {
        "type": "mcq",
        "question": "What is the effect of calling `setEditable(false)` on a `JTextField` component?",
        "options": [
            "It disables the text field so that it cannot gain focus.",
            "It makes the text field read-only but still allows text selection.",
            "It hides the text field from the UI.",
            "It clears the text inside the text field.",
            "It changes the background color to gray."
        ],
        "answer": "B",
        "explanation": "`setEditable(false)` makes the text field read-only; users cannot edit the text but can select it."
    },
    {
        "type": "mcq",
        "question": "Which method of `JComboBox` would you use to add a new item to the combo box?",
        "options": [
            "addItem(Object item)",
            "insertItemAt(Object item, int index)",
            "add(Object item)",
            "putItem(Object item)",
            "appendItem(Object item)"
        ],
        "answer": "A",
        "explanation": "`addItem(Object item)` adds a new item to the end of the `JComboBox`."
    },
    {
        "type": "mcq",
        "question": "What is the purpose of the `javax.swing.Timer` class in Java Swing?",
        "options": [
            "To schedule a task for execution after a given delay.",
            "To measure the time elapsed during an operation.",
            "To perform an action at regular intervals on the Event Dispatch Thread.",
            "To manage the frame rate of animations.",
            "To provide a countdown timer for user interfaces."
        ],
        "answer": "C",
        "explanation": "`javax.swing.Timer` performs an action at regular intervals on the Event Dispatch Thread."
    },
    {
        "type": "mcq",
        "question": "Which of the following exceptions is a subclass of `RuntimeException`?",
        "options": [
            "IOException",
            "FileNotFoundException",
            "ArithmeticException",
            "InterruptedException",
            "Exception"
        ],
        "answer": "C",
        "explanation": "`ArithmeticException` is a subclass of `RuntimeException`."
    },
    {
        "type": "mcq",
        "question": "Which `Character` class method would you use to check if a character is an uppercase letter?",
        "options": [
            "Character.isLetter(char ch)",
            "Character.isUpperCase(char ch)",
            "Character.isDigit(char ch)",
            "Character.isWhitespace(char ch)",
            "Character.isAlphabetic(char ch)"
        ],
        "answer": "B",
        "explanation": "`Character.isUpperCase(char ch)` returns `true` if the character is uppercase."
    },
    {
        "type": "mcq",
        "question": "What exception is thrown by `Integer.parseInt(String s)` if the string cannot be parsed as an integer?",
        "options": [
            "NumberFormatException",
            "InputMismatchException",
            "IllegalArgumentException",
            "NullPointerException",
            "ArithmeticException"
        ],
        "answer": "A",
        "explanation": "`Integer.parseInt` throws `NumberFormatException` if the string is not a valid integer."
    },
    {
        "type": "mcq",
        "question": "Which method of `JFileChooser` displays the dialog for opening a file?",
        "options": [
            "showOpenDialog(Component parent)",
            "showSaveDialog(Component parent)",
            "showDialog(Component parent, String approveButtonText)",
            "openDialog(Component parent)",
            "displayOpenDialog(Component parent)"
        ],
        "answer": "A",
        "explanation": "`showOpenDialog(Component parent)` displays the file open dialog."
    },
    {
        "type": "mcq",
        "question": "Which of the following components can have an `ActionListener` added to it using `addActionListener`?",
        "options": [
            "JButton",
            "JLabel",
            "JPanel",
            "JScrollPane",
            "JFrame"
        ],
        "answer": "A",
        "explanation": "`JButton` can have an `ActionListener` added; it generates action events."
    },
    {
        "type": "mcq",
        "question": "What happens when you add more components than the specified number of cells in a `GridLayout`?",
        "options": [
            "An exception is thrown.",
            "Extra components are not displayed.",
            "The layout adds extra rows or columns to accommodate the components.",
            "Components overlap in the same cells.",
            "The layout manager ignores the extra components."
        ],
        "answer": "C",
        "explanation": "`GridLayout` expands to accommodate all components by adding rows or columns."
    },
    {
        "type": "mcq",
        "question": "What is the purpose of calling `setPreferredSize(Dimension d)` on a component?",
        "options": [
            "To set the component's maximum size.",
            "To set the component's preferred size, which the layout manager may use.",
            "To fix the component's size, overriding the layout manager.",
            "To set the component's minimum size.",
            "To resize the component to fill the container."
        ],
        "answer": "B",
        "explanation": "`setPreferredSize(Dimension d)` suggests a preferred size to the layout manager."
    },
    {
        "type": "mcq",
        "question": "Why is it important to create and modify Swing components on the Event Dispatch Thread (EDT)?",
        "options": [
            "Because Swing components are not thread-safe.",
            "To improve performance.",
            "To prevent deadlocks.",
            "Because the EDT handles file I/O.",
            "Because the EDT can handle network operations."
        ],
        "answer": "A",
        "explanation": "Swing components are not thread-safe; modifying them on the EDT prevents concurrency issues."
    },
    {
        "type": "mcq",
        "question": "What is the result of the following code snippet?\n\n```java\nString str = \"apple,banana,,orange,,\";\nString[] parts = str.split(\",\");\nSystem.out.println(parts.length);\n```",
        "options": [
            "3",
            "4",
            "5",
            "6",
            "Compilation error"
        ],
        "answer": "C",
        "explanation": "The `split` method splits at commas. Empty strings between commas are counted. The array length is 5."
    },
    {
        "type": "mcq",
        "question": "Which exception is a checked exception and must be either caught or declared in the method signature?",
        "options": [
            "NullPointerException",
            "ArithmeticException",
            "IOException",
            "IndexOutOfBoundsException",
            "RuntimeException"
        ],
        "answer": "C",
        "explanation": "`IOException` is a checked exception; it must be caught or declared."
    },
    {
        "type": "mcq",
        "question": "What is the range of values returned by `Math.random()` in Java?",
        "options": [
            "0.0 (inclusive) to 1.0 (exclusive)",
            "0.0 (exclusive) to 1.0 (inclusive)",
            "0.0 (inclusive) to 1.0 (inclusive)",
            "0.0 (exclusive) to 1.0 (exclusive)",
            "-1.0 (inclusive) to 1.0 (inclusive)"
        ],
        "answer": "A",
        "explanation": "`Math.random()` returns a value between 0.0 (inclusive) and 1.0 (exclusive)."
    },
    {
        "type": "mcq",
        "question": "What is the advantage of implementing the `AutoCloseable` interface in Java?",
        "options": [
            "It allows the object to be used with the `try-with-resources` statement for automatic resource management.",
            "It ensures that the object cannot be serialized.",
            "It provides thread safety for the object.",
            "It prevents memory leaks by forcing garbage collection.",
            "It allows the object to be cloned."
        ],
        "answer": "A",
        "explanation": "`AutoCloseable` enables the object to be used in a `try-with-resources` statement."
    },
    {
        "type": "mcq",
        "question": "Which method would you use to get the current value of a `JSlider` component?",
        "options": [
            "getValue()",
            "getCurrentValue()",
            "getPosition()",
            "getSliderValue()",
            "getSelectedValue()"
        ],
        "answer": "A",
        "explanation": "`getValue()` returns the current value of a `JSlider`."
    },
    {
        "type": "mcq",
        "question": "When implementing the `KeyListener` interface, which method is called when a key is typed (pressed and released)?",
        "options": [
            "keyPressed(KeyEvent e)",
            "keyReleased(KeyEvent e)",
            "keyTyped(KeyEvent e)",
            "keyClicked(KeyEvent e)",
            "keyEntered(KeyEvent e)"
        ],
        "answer": "C",
        "explanation": "`keyTyped(KeyEvent e)` is called when a key is pressed and released."
    },
    {
        "type": "mcq",
        "question": "Which method of `JTextArea` allows you to add text to the end of the current content?",
        "options": [
            "setText(String text)",
            "append(String text)",
            "insert(String text, int pos)",
            "addText(String text)",
            "updateText(String text)"
        ],
        "answer": "B",
        "explanation": "`append(String text)` adds text to the end of a `JTextArea`."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code?\n\n```java\npublic class Test {\n    public static int factorial(int n) {\n        if (n == 0) return 1;\n        else return n * factorial(n - 1);\n    }\n    public static void main(String[] args) {\n        System.out.println(factorial(5));\n    }\n}\n```",
        "options": [
            "120",
            "60",
            "24",
            "5",
            "1"
        ],
        "answer": "A",
        "explanation": "The factorial of 5 is calculated as 5 * 4 * 3 * 2 * 1 = 120."
    },
    {
        "type": "mcq",
        "question": "Given the following code for tree traversal, what type of traversal is being performed?\n\n```java\npublic void traverse(Node node) {\n    if (node != null) {\n        traverse(node.left);\n        System.out.print(node.data + \" \");\n        traverse(node.right);\n    }\n}\n```",
        "options": [
            "Pre-order traversal",
            "In-order traversal",
            "Post-order traversal",
            "Level-order traversal",
            "Depth-first traversal"
        ],
        "answer": "B",
        "explanation": "In-order traversal visits the left subtree, then the node, and finally the right subtree."
    },
    {
        "type": "mcq",
        "question": "What does the following Java Stream code output?\n\n```java\nList<String> words = Arrays.asList(\"apple\", \"banana\", \"avocado\", \"cherry\");\nlong count = words.stream()\n    .filter(w -> w.startsWith(\"a\"))\n    .count();\nSystem.out.println(count);\n```",
        "options": [
            "1",
            "2",
            "3",
            "4",
            "0"
        ],
        "answer": "B",
        "explanation": "\"apple\" and \"avocado\" start with 'a', so the count is 2."
    },
    {
        "type": "mcq",
        "question": "Given the following code using `Optional`, what will be the output?\n\n```java\nOptional<String> opt = Optional.ofNullable(null);\nSystem.out.println(opt.isPresent());\n```",
        "options": [
            "true",
            "false",
            "null",
            "Compilation error",
            "Throws NullPointerException"
        ],
        "answer": "B",
        "explanation": "Since the value is null, `opt` is an empty `Optional`, so `isPresent()` returns false."
    },
    {
        "type": "mcq",
        "question": "Which of the following best describes backtracking in recursive algorithms?",
        "options": [
            "Exploring all possible options and undoing choices when a dead end is reached.",
            "Dividing the problem into smaller subproblems and combining their results.",
            "Using a stack data structure to keep track of function calls.",
            "Optimizing the solution by memorizing intermediate results.",
            "Iteratively improving the solution until a stopping condition is met."
        ],
        "answer": "A",
        "explanation": "Backtracking involves trying different paths and reverting when a path doesn't lead to a solution."
    },
    {
        "type": "mcq",
        "question": "Which property is NOT a characteristic of a red-black tree?",
        "options": [
            "Every node is either red or black.",
            "The root is always black.",
            "All leaves are red.",
            "No two red nodes can be adjacent.",
            "Every path from a node to its descendant leaves contains the same number of black nodes."
        ],
        "answer": "C",
        "explanation": "In red-black trees, all leaves (null nodes) are considered black, not red."
    },
    {
        "type": "mcq",
        "question": "What is the time complexity of the Heapsort algorithm?",
        "options": [
            "O(n)",
            "O(n log n)",
            "O(n^2)",
            "O(log n)",
            "O(n^2 log n)"
        ],
        "answer": "B",
        "explanation": "Heapsort has a time complexity of O(n log n) for all cases."
    },
    {
        "type": "mcq",
        "question": "Given the following lambda expression, what does it compute?\n\n```java\n(int x, int y) -> x < y ? x : y\n```",
        "options": [
            "The maximum of x and y",
            "The minimum of x and y",
            "The sum of x and y",
            "Always returns x",
            "Always returns y"
        ],
        "answer": "B",
        "explanation": "The lambda expression returns the smaller of x and y."
    },
    {
        "type": "mcq",
        "question": "In a UML class diagram, which symbol represents an aggregation relationship?",
        "options": [
            "A solid line with an open diamond",
            "A dashed line with an open arrow",
            "A solid line with a closed arrow",
            "A solid line with a filled diamond",
            "A solid line without any decorations"
        ],
        "answer": "A",
        "explanation": "An aggregation is depicted with a solid line and an open diamond pointing to the whole from the part."
    },
    {
        "type": "mcq",
        "question": "Given the following class definitions, what type of relationship exists between `Car` and `Engine`?\n\n```java\npublic class Engine {\n    // Engine properties\n}\n\npublic class Car {\n    private Engine engine;\n    // Car properties\n}\n```",
        "options": [
            "Inheritance",
            "Aggregation",
            "Composition",
            "Association",
            "Dependency"
        ],
        "answer": "C",
        "explanation": "Composition implies that `Car` owns `Engine`, and `Engine` cannot exist without `Car`."
    },
    {
        "type": "mcq",
        "question": "Consider the following code. What will be the output?\n\n```java\nclass Animal {\n    public void makeSound() {\n        System.out.println(\"Some generic animal sound\");\n    }\n}\n\nclass Dog extends Animal {\n    public void makeSound() {\n        System.out.println(\"Bark\");\n    }\n}\n\npublic class Test {\n    public static void main(String[] args) {\n        Animal myDog = new Dog();\n        myDog.makeSound();\n    }\n}\n```",
        "options": [
            "Some generic animal sound",
            "Bark",
            "Compilation error",
            "Runtime error",
            "No output"
        ],
        "answer": "B",
        "explanation": "Due to method overriding, `makeSound()` in `Dog` is called, outputting \"Bark\"."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code?\n\n```java\nList<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);\nint sum = numbers.stream()\n    .filter(n -> n % 2 == 0)\n    .mapToInt(n -> n * n)\n    .sum();\nSystem.out.println(sum);\n```",
        "options": [
            "20",
            "54",
            "4",
            "29",
            "30"
        ],
        "answer": "A",
        "explanation": "Even numbers are 2 and 4; their squares are 4 and 16; sum is 20."
    },
    {
        "type": "mcq",
        "question": "Given the following code using `Collectors.groupingBy`, what is the result?\n\n```java\nList<String> words = Arrays.asList(\"apple\", \"apricot\", \"banana\", \"blueberry\", \"avocado\");\nMap<Character, List<String>> groups = words.stream()\n    .collect(Collectors.groupingBy(w -> w.charAt(0)));\nSystem.out.println(groups.get('a').size());\n```",
        "options": [
            "1",
            "2",
            "3",
            "4",
            "0"
        ],
        "answer": "C",
        "explanation": "Words starting with 'a' are \"apple\", \"apricot\", \"avocado\"; size is 3."
    },
    {
        "type": "mcq",
        "question": "What will happen when the following recursive method is called with `countDown(5)`?\n\n```java\npublic void countDown(int n) {\n    System.out.println(n);\n    countDown(n - 1);\n}\n```",
        "options": [
            "Prints numbers from 5 to 1",
            "Prints numbers from 5 to -infinity",
            "Throws StackOverflowError",
            "Compilation error",
            "Prints nothing"
        ],
        "answer": "C",
        "explanation": "The method lacks a base case, leading to infinite recursion and a `StackOverflowError`."
    },
    {
        "type": "mcq",
        "question": "Which of the following statements best describes the difference between association, aggregation, and composition in UML diagrams?",
        "options": [
            "Association is a 'has-a' relationship, aggregation is a 'part-of' relationship, composition is a 'uses-a' relationship.",
            "Association is a 'uses-a' relationship, aggregation is a 'has-a' relationship, composition is a 'part-of' relationship.",
            "Association is a 'part-of' relationship, aggregation is a 'uses-a' relationship, composition is a 'has-a' relationship.",
            "Association, aggregation, and composition all represent the same type of relationship.",
            "Composition is a stronger form of aggregation where the lifetime of the part is bound to the whole."
        ],
        "answer": "E",
        "explanation": "Composition is a strong form of aggregation; the part cannot exist independently of the whole."
    },
    {
        "type": "mcq",
        "question": "Which traversal method visits the root node first, then recursively visits the left subtree, and finally the right subtree?",
        "options": [
            "In-order traversal",
            "Pre-order traversal",
            "Post-order traversal",
            "Level-order traversal",
            "Depth-first traversal"
        ],
        "answer": "B",
        "explanation": "Pre-order traversal processes the root before its subtrees."
    },
    {
        "type": "mcq",
        "question": "Which of the following is a property of a red-black tree?",
        "options": [
            "It is always perfectly balanced.",
            "Every red node must have black children.",
            "All leaves are red.",
            "Every node must be either red or green.",
            "Red nodes cannot have black parents."
        ],
        "answer": "B",
        "explanation": "In red-black trees, a red node cannot have red children."
    },
    {
        "type": "mcq",
        "question": "What is the primary difference between depth-first search (DFS) and breadth-first search (BFS) in tree traversal?",
        "options": [
            "DFS uses a queue; BFS uses a stack.",
            "DFS explores nodes level by level; BFS explores as far as possible along each branch.",
            "DFS uses more memory than BFS.",
            "DFS explores as far as possible along each branch before backtracking; BFS explores nodes level by level.",
            "There is no difference between DFS and BFS."
        ],
        "answer": "D",
        "explanation": "DFS goes deep into a branch before backtracking; BFS explores all neighbors at the current depth."
    },
    {
        "type": "mcq",
        "question": "Which of the following best describes how backtracking works in solving problems like mazes?",
        "options": [
            "It explores all possible paths simultaneously.",
            "It uses heuristics to choose the best path.",
            "It tries one path, and if it fails, it backtracks and tries another path.",
            "It uses random choices to find the solution.",
            "It solves the problem by dividing it into subproblems and combining the results."
        ],
        "answer": "C",
        "explanation": "Backtracking involves exploring paths and reverting when a dead end is reached."
    },
    {
        "type": "mcq",
        "question": "What is a key advantage of using Java Streams for processing collections?",
        "options": [
            "They always execute faster than loops.",
            "They provide a declarative approach to processing data with operations like map, filter, and reduce.",
            "They automatically parallelize code.",
            "They eliminate the need for exception handling.",
            "They can process only sequential data."
        ],
        "answer": "B",
        "explanation": "Streams offer a declarative way to process data, making code more concise and readable."
    },
    {
        "type": "mcq",
        "question": "Which method fills an `IntStream` with a sequence of numbers from 0 to 9?",
        "options": [
            "IntStream.range(0, 10)",
            "IntStream.of(0, 10)",
            "IntStream.generate(() -> 10)",
            "IntStream.iterate(0, i -> i + 1).limit(9)",
            "IntStream.rangeClosed(0, 9)"
        ],
        "answer": "A",
        "explanation": "`IntStream.range(0, 10)` generates numbers from 0 (inclusive) to 10 (exclusive), i.e., 0 to 9."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code?\n\n```java\nimport java.util.Optional;\npublic class Test {\n    public static void main(String[] args) {\n        Optional<String> opt = Optional.empty();\n        System.out.println(opt.orElse(\"Default\"));\n    }\n}\n```",
        "options": [
            "null",
            "Default",
            "Compilation error",
            "Runtime error",
            "Cannot be determined"
        ],
        "answer": "B",
        "explanation": "Since the `Optional` is empty, the `orElse` method provides the default value \"Default\"."
    },
    {
        "type": "mcq",
        "question": "What is the output of the following code?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        String s = \"Java\";\n        System.out.println(s.repeat(3));\n    }\n}\n```",
        "options": [
            "\"JavaJavaJava\"",
            "\"Java\"",
            "\"Java Java Java\"",
            "Compilation error",
            "Runtime error"
        ],
        "answer": "A",
        "explanation": "The `repeat` method repeats the string three times, resulting in \"JavaJavaJava\"."
    },
    {
        "type": "mcq",
        "question": "What will the following code output?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        int x = 0;\n        x = x++ + ++x;\n        System.out.println(x);\n    }\n}\n```",
        "options": [
            "0",
            "1",
            "2",
            "3",
            "Compilation error"
        ],
        "answer": "C",
        "explanation": "`x++` uses the value of `x` before incrementing, and `++x` increments before using the value. Calculation: `x = 0 + 2` results in `x = 2`."
    },
    {
        "type": "mcq",
        "question": "What will happen if the following code is executed?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        Integer x = null;\n        int y = x;\n        System.out.println(y);\n    }\n}\n```",
        "options": [
            "null",
            "0",
            "Runtime NullPointerException",
            "Compilation error",
            "Cannot be determined"
        ],
        "answer": "C",
        "explanation": "Unboxing a `null` Integer to a primitive type throws a `NullPointerException`."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code?\n\n```java\npublic class Test {\n    public static void main(String[] args) {\n        int[] arr = {1, 2, 3, 4, 5};\n        int result = Arrays.stream(arr).reduce(0, (a, b) -> a - b);\n        System.out.println(result);\n    }\n}\n```",
        "options": [
            "-15",
            "-13",
            "-5",
            "0",
            "Compilation error"
        ],
        "answer": "B",
        "explanation": "The reduction operation starts with 0 and subtracts each element: `0 - 1 - 2 - 3 - 4 - 5 = -15`."
    },
    {
        "type": "mcq",
        "question": "What will the following code output?\n\n```java\nimport java.util.concurrent.*;\n\npublic class Test {\n    public static void main(String[] args) {\n        ExecutorService executor = Executors.newFixedThreadPool(2);\n        executor.execute(() -> System.out.println(\"Task 1\"));\n        executor.execute(() -> System.out.println(\"Task 2\"));\n        executor.shutdown();\n        executor.execute(() -> System.out.println(\"Task 3\"));\n    }\n}\n```",
        "options": [
            "Task 1\nTask 2\nTask 3",
            "Task 1\nTask 2",
            "Task 1\nTask 2\nRuntime exception",
            "Compilation error",
            "Cannot be determined"
        ],
        "answer": "C",
        "explanation": "The `shutdown` method stops new tasks from being submitted. Attempting to submit `Task 3` after shutdown throws `RejectedExecutionException`."
    },
    {
        "type": "mcq",
        "question": "What will be the output of the following code?\n\n```java\nimport java.util.*;\npublic class Test {\n    public static void main(String[] args) {\n        Map<String, Integer> map = new LinkedHashMap<>();\n        map.put(\"A\", 1);\n        map.put(\"B\", 2);\n        map.put(\"C\", 3);\n        map.put(\"A\", 4);\n        System.out.println(map);\n    }\n}\n```",
        "options": [
            "{A=1, B=2, C=3}",
            "{A=4, B=2, C=3}",
            "{A=1, B=2, C=3, A=4}",
            "Compilation error",
            "Runtime error"
        ],
        "answer": "B",
        "explanation": "In a `LinkedHashMap`, duplicate keys overwrite the previous value. The final map is `{A=4, B=2, C=3}`."
    },
    {
        "type": "mcq",
        "question": "Which of the following best describes the difference between `ConcurrentHashMap` and `HashMap` in Java?",
        "options": [
            "`ConcurrentHashMap` allows null keys, `HashMap` does not.",
            "`ConcurrentHashMap` is thread-safe, `HashMap` is not.",
            "`ConcurrentHashMap` preserves insertion order, `HashMap` does not.",
            "`HashMap` uses locks for synchronization, `ConcurrentHashMap` does not.",
            "There is no difference."
        ],
        "answer": "B",
        "explanation": "`ConcurrentHashMap` is thread-safe for concurrent access, while `HashMap` is not."
    },
    {
        "type": "mcq",
        "question": "What will the following code print?\n\n```java\nint n = 1;\nint m = -1;\nif (n < -m) { System.out.print(n); }\nelse { System.out.print(m); }\n```",
        "options": [
            "1",
            "-1",
            "Compilation error",
            "Runtime error",
            "None of the above"
        ],
        "answer": "B",
        "explanation": "`-m` evaluates to `1`, so the condition `n < -m` is `false`. Therefore, the else branch executes, printing `-1`."
    },
    {
        "type": "mcq",
        "question": "What will the following code fragment output?\n\n```java\ndouble x = Math.sqrt(2);\ndouble y = 2;\nif (x * x == y) { System.out.print(x); }\nelse { System.out.print(y); }\n```",
        "options": [
            "1.41421356237",
            "2",
            "Compilation error",
            "Runtime error",
            "None of the above"
        ],
        "answer": "B",
        "explanation": "Due to floating-point precision issues, `x * x` does not exactly equal `y`. Therefore, the else branch executes, printing `2`."
    },
    {
        "type": "mcq",
        "question": "Which of the following pseudocode correctly calculates if two appointments overlap?\n\nAppointment 1: start1 to end1\nAppointment 2: start2 to end2\n\n",
        "options": [
            "If (start1 <= start2 AND end1 >= end2) then overlap.",
            "If (start2 <= start1 AND end2 >= end1) then overlap.",
            "If (start1 < end2 AND start2 < end1) then overlap.",
            "If (start1 >= end2 OR start2 >= end1) then overlap.",
            "None of the above."
        ],
        "answer": "C",
        "explanation": "The condition checks if the intervals overlap by verifying that the start time of one appointment is before the end time of the other."
    },
    {
        "type": "mcq",
        "question": "What error will the following code produce?\n\n```java\nif (floor = 13) {\n    System.out.println(\"Lucky number!\");\n}\n```",
        "options": [
            "Assignment in conditional is not allowed.",
            "The `=` operator cannot be used in conditionals.",
            "Compilation error: incompatible types.",
            "Runtime error.",
            "No error; the code runs fine."
        ],
        "answer": "C",
        "explanation": "The assignment operator `=` cannot be used in a conditional because it does not evaluate to a boolean."
    },
    {
        "type": "mcq",
        "question": "What will the following pseudocode output?\n\n```\nInput: letter = g, number = 5\nIf letter is a, c, e, g\n    If number is odd: color = black\n    Else: color = white\nElse\n    If number is even: color = black\n    Else: color = white\nPrint color.\n```",
        "options": [
            "white",
            "black",
            "light",
            "dark",
            "None of the above"
        ],
        "answer": "B",
        "explanation": "The letter `g` and the number `5` satisfy the first condition (odd number), so the square is `black`."
    },
    {
        "type": "mcq",
        "question": "Which of the following Java expressions checks if two pixels `(x1, y1)` and `(x2, y2)` are within a distance of less than 5?\n\n",
        "options": [
            "`Math.abs(x1 - x2) < 5 && Math.abs(y1 - y2) < 5`",
            "`Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) < 5`",
            "`Math.abs((x1 + x2) + (y1 + y2)) < 5`",
            "`(x1 - x2) + (y1 - y2) < 5`",
            "`None of the above`"
        ],
        "answer": "B",
        "explanation": "The Euclidean distance formula calculates the straight-line distance between two points. Checking if it's less than 5 determines closeness."
    },
    {
        "type": "mcq",
        "question": "What will the following pseudocode output for the month and day input `7` and `4`?\n\n```\nInput: month, day\nIf month = 1 AND day = 1\n    Print \"New Year’s Day\"\nElse If month = 7 AND day = 4\n    Print \"Independence Day\"\nElse If month = 11 AND day = 11\n    Print \"Veterans Day\"\nElse If month = 12 AND day = 25\n    Print \"Christmas Day\"\nElse\n    Print \"Not a holiday\"\n```",
        "options": [
            "New Year’s Day",
            "Independence Day",
            "Veterans Day",
            "Christmas Day",
            "Not a holiday"
        ],
        "answer": "B",
        "explanation": "The input `7` and `4` matches the condition for `Independence Day`."
    },
    {
        "type": "mcq",
        "question": "What will the following code snippet print?\n\n```java\nint result = 1;\nfor (int i = 5; i > 0; i--) {\n    result = result * i;\n}\nSystem.out.println(result);\n```",
        "options": [
            "120",
            "15",
            "1",
            "25",
            "Compilation error"
        ],
        "answer": "A",
        "explanation": "The loop calculates the factorial of 5: `5 * 4 * 3 * 2 * 1 = 120`."
    },
    {
        "type": "mcq",
        "question": "What is the result of this loop?\n\n```java\nint i = 0;\nwhile (i < 10) {\n    if (i % 2 == 0) {\n        System.out.print(\"*\");\n    } else {\n        System.out.print(\"-\");\n    }\n    i++;\n}\n```",
        "options": [
            "*-*-*-*-*-*",
            "*-*",
            "**********",
            "-----",
            "Compilation error"
        ],
        "answer": "A",
        "explanation": "The loop alternates printing `*` and `-` for each value of `i` up to 9."
    },
    {
        "type": "mcq",
        "question": "Which of the following pseudocode correctly computes the sum of all squares less than `n`?\n",
        "options": [
            "```java\nint i = 0;\nint sum = 0;\nwhile (i * i < n) {\n    sum += i;\n    i++;\n}\n```",
            "```java\nint i = 0;\nint sum = 0;\nwhile (i * i < n) {\n    sum += i * i;\n    i++;\n}\n```",
            "```java\nint i = 0;\nint sum = 0;\nfor (int i = 0; i * i < n; i++) {\n    sum += i * i;\n}\n```",
            "```java\nint sum = 0;\nwhile (i * i < n) {\n    sum = i * i;\n}\n```",
            "None of the above"
        ],
        "answer": "B",
        "explanation": "The correct loop adds `i * i` to `sum` for each value of `i` until `i * i >= n`."
    },
    {
        "type": "mcq",
        "question": "What is the value of `n` after executing this loop?\n\n```java\nint i = 1;\nint n = 0;\nwhile (i <= 10) {\n    n += i;\n    i++;\n}\n```",
        "options": [
            "45",
            "55",
            "10",
            "11",
            "Compilation error"
        ],
        "answer": "B",
        "explanation": "The loop calculates the sum of integers from 1 to 10, which is `55`."
    },
    {
        "type": "mcq",
        "question": "What is an 'off-by-one' error in the context of loops?",
        "options": [
            "A loop that executes one too many iterations.",
            "A loop that skips an iteration.",
            "A loop that terminates early.",
            "A loop that cannot compile due to a syntax error.",
            "A loop that never initializes the counter."
        ],
        "answer": "A",
        "explanation": "An 'off-by-one' error occurs when a loop iterates one time too many or too few due to incorrect initialization or condition."
    },
    {
        "type": "mcq",
        "question": "Which of the following best describes a sentinel value in Java?",
        "options": [
            "A value that indicates the end of a loop or sequence.",
            "A constant used to control loop execution.",
            "A placeholder for uninitialized variables.",
            "A value used for error handling.",
            "None of the above"
        ],
        "answer": "A",
        "explanation": "A sentinel value is a special value used to signal the termination of a loop or input sequence."
    },
    {
        "type": "mcq",
        "question": "What is the output of the following loop?\n\n```java\nfor (int i = 10; i >= 1; i /= 2) {\n    System.out.print(i + \" \");\n}\n```",
        "options": [
            "10 5 2 1",
            "10 5 2",
            "10 5",
            "10",
            "Compilation error"
        ],
        "answer": "A",
        "explanation": "The loop halves `i` in each iteration until `i` becomes less than 1. The output is `10 5 2 1`."
    },
    {
        "type": "mcq",
        "question": "What will the following code snippet output?\n\n```java\npublic static void main(String[] args) {\n    int x = 3;\n    int y = 4;\n    falseSwap(x, y);\n    System.out.println(x + \" \" + y);\n}\n\npublic static void falseSwap(int a, int b) {\n    int temp = a;\n    a = b;\n    b = temp;\n}\n```",
        "options": [
            "3 4",
            "4 3",
            "0 0",
            "Compilation error",
            "Runtime error"
        ],
        "answer": "A",
        "explanation": "Java passes arguments by value, so changes to `a` and `b` inside `falseSwap` do not affect the original `x` and `y`."
    },
    {
        "type": "mcq",
        "question": "What is the scope of the variable `b` in the following method?\n\n```java\npublic static int g(int a) {\n    int b = 0;\n    for (int n = 0; n < a; n++) {\n        int i = f(n);\n        b = b + i;\n    }\n    return b;\n}\n```",
        "options": [
            "Global scope",
            "Class scope",
            "Method scope",
            "Block scope",
            "Package scope"
        ],
        "answer": "C",
        "explanation": "The variable `b` is declared within the method `g`, so it has method scope and is accessible throughout the method."
    },
    {
        "type": "mcq",
        "question": "Which of the following is true about recursive methods in Java?",
        "options": [
            "Recursive methods always terminate.",
            "Recursive methods must have a base case.",
            "Recursive methods cannot use loops.",
            "Recursive methods always return a value.",
            "Recursive methods execute faster than iterative methods."
        ],
        "answer": "B",
        "explanation": "A recursive method must include a base case to prevent infinite recursion."
    },
    {
        "type": "mcq",
        "question": "What is the output of the following method calls?\n\n```java\npublic static double f(double x) { return g(x) + Math.sqrt(h(x)); }\npublic static double g(double x) { return 4 * h(x); }\npublic static double h(double x) { return x * x + k(x) - 1; }\npublic static double k(double x) { return 2 * (x + 1); }\n\nSystem.out.println(f(2));\n```",
        "options": [
            "24.0",
            "28.0",
            "29.0",
            "30.0",
            "Compilation error"
        ],
        "answer": "C",
        "explanation": "Breaking down: `k(2) = 6`, `h(2) = 2 * 2 + 6 - 1 = 9`, `g(2) = 4 * 9 = 36`, `f(2) = 36 + sqrt(9) = 36 + 3 = 39`."
    },
    {
        "type": "mcq",
        "question": "What is the purpose of a return statement in Java methods?",
        "options": [
            "To terminate the program execution.",
            "To exit the current loop.",
            "To specify the value a method should pass back to the caller.",
            "To execute another method.",
            "To print a message to the console."
        ],
        "answer": "C",
        "explanation": "The return statement specifies the value to pass back to the caller and immediately exits the method."
    },
    {
        "type": "mcq",
        "question": "What is wrong with the following program?\n\n```java\npublic static void main(String[] args) {\n    System.out.print(\"What is your name? \");\n    String input = in.next();\n    System.out.println(\"Hello, \" + input);\n    System.out.print(\"How old are you? \");\n    int input = in.nextInt();\n    input++;\n    System.out.println(\"Next year, you will be \" + input);\n}\n```",
        "options": [
            "The variable `input` is redeclared.",
            "The program has a syntax error in the `System.out.print` statement.",
            "The `Scanner` object is not defined.",
            "The `main` method must return an integer.",
            "Nothing is wrong; the program runs correctly."
        ],
        "answer": "A",
        "explanation": "The variable `input` is declared twice in the same scope, which is not allowed in Java."
    },
    {
        "type": "mcq",
        "question": "Which of the following best describes stepwise refinement?",
        "options": [
            "Breaking a problem into smaller, manageable pieces.",
            "Writing code without any pre-defined structure.",
            "Optimizing a method by reducing its runtime.",
            "Using recursion to solve all problems.",
            "Writing pseudocode for all algorithms."
        ],
        "answer": "A",
        "explanation": "Stepwise refinement involves breaking a problem into smaller pieces and solving each step systematically."
    },
    {
        "type": "mcq",
        "question": "What is the output of the following code snippet?\n\n```java\nint[] values = {1, 2, 3, 4, 5, 4, 3, 2, 1, 0};\nint total = 0;\nfor (int i = 9; i >= 0; i--) {\n    total = total + values[i];\n}\nSystem.out.println(total);\n```",
        "options": [
            "20",
            "25",
            "30",
            "35",
            "40"
        ],
        "answer": "B",
        "explanation": "The loop sums all elements of the array. The total is 1 + 2 + 3 + 4 + 5 + 4 + 3 + 2 + 1 + 0 = 25."
    },
    {
        "type": "mcq",
        "question": "Which of the following code snippets correctly initializes a two-dimensional array with alternating 0s and 1s in a checkerboard pattern?",
        "options": [
            "```java\nint[][] values = new int[3][3];\nfor (int i = 0; i < 3; i++) {\n    for (int j = 0; j < 3; j++) {\n        values[i][j] = (i + j) % 2;\n    }\n}\n```",
            "```java\nint[][] values = new int[3][3];\nfor (int i = 0; i < 3; i++) {\n    for (int j = 0; j < 3; j++) {\n        values[i][j] = (i * j) % 2;\n    }\n}\n```",
            "```java\nint[][] values = new int[3][3];\nfor (int i = 0; i < 3; i++) {\n    for (int j = 0; j < 3; j++) {\n        values[i][j] = i % 2;\n    }\n}\n```",
            "```java\nint[][] values = new int[3][3];\nfor (int i = 0; i < 3; i++) {\n    for (int j = 0; j < 3; j++) {\n        values[i][j] = j % 2;\n    }\n}\n```",
            "None of the above"
        ],
        "answer": "A",
        "explanation": "The expression `(i + j) % 2` alternates between 0 and 1 to create a checkerboard pattern."
    },
    {
        "type": "mcq",
        "question": "What is the purpose of the `ArrayList` method `add(E e)`?",
        "options": [
            "To remove an element from the list.",
            "To retrieve an element at a specific index.",
            "To add an element to the end of the list.",
            "To check if the list contains a specific element.",
            "To replace an element at a specific index."
        ],
        "answer": "C",
        "explanation": "The `add(E e)` method appends the specified element to the end of the list."
    },
    {
        "type": "mcq",
        "question": "Which of the following correctly describes an array index in Java?",
        "options": [
            "The index starts at 1 and goes up to the array's length.",
            "The index starts at 0 and goes up to the array's length - 1.",
            "The index starts at 0 and can exceed the array's length.",
            "The index is automatically set to the array's length.",
            "There is no concept of an index in Java arrays."
        ],
        "answer": "B",
        "explanation": "Array indices in Java are zero-based, starting from 0 and ending at `length - 1`."
    },
    {
        "type": "mcq",
        "question": "What is the time complexity of accessing an element in an array by its index?",
        "options": [
            "O(n)",
            "O(log n)",
            "O(1)",
            "O(n^2)",
            "O(n log n)"
        ],
        "answer": "C",
        "explanation": "Accessing an element by its index in an array takes constant time, O(1)."
    },
    {
        "type": "mcq",
        "question": "What will be the result of the following code snippet?\n\n```java\nArrayList<Integer> values = new ArrayList<>();\nfor (int i = 1; i <= 5; i++) {\n    values.add(i * i);\n}\nSystem.out.println(values);\n```",
        "options": [
            "[1, 4, 9, 16, 25]",
            "[1, 2, 3, 4, 5]",
            "[0, 1, 4, 9, 16, 25]",
            "[1, 2, 4, 8, 16]",
            "Compilation error"
        ],
        "answer": "A",
        "explanation": "The loop adds the squares of 1 through 5 to the list, resulting in [1, 4, 9, 16, 25]."
    },
    {
        "type": "mcq",
        "question": "Which of the following is a true statement about array bounds errors in Java?",
        "options": [
            "Array bounds errors are caught at compile time.",
            "Array bounds errors are ignored, and the program continues.",
            "Array bounds errors throw an `ArrayIndexOutOfBoundsException` at runtime.",
            "Array bounds errors automatically adjust the size of the array.",
            "Array bounds errors are only checked when debugging."
        ],
        "answer": "C",
        "explanation": "Accessing an invalid index in an array causes an `ArrayIndexOutOfBoundsException` at runtime."
    },
    {
        "type": "mcq",
        "question": "What is the output of the following code snippet?\n\n```java\nint[][] values = new int[2][3];\nfor (int i = 0; i < 2; i++) {\n    for (int j = 0; j < 3; j++) {\n        values[i][j] = i + j;\n    }\n}\nSystem.out.println(values[1][2]);\n```",
        "options": [
            "2",
            "3",
            "4",
            "5",
            "Compilation error"
        ],
        "answer": "B",
        "explanation": "The value at `values[1][2]` is `1 + 2 = 3`."
    },
    {
        "type": "mcq",
        "question": "In an object-oriented traffic simulation system, which of the following inheritance relationships is correct?",
        "options": [
            "Sedan extends Coupe",
            "Truck extends Car",
            "Car extends Vehicle",
            "Bicycle extends Motorcycle",
            "Vehicle extends Minivan"
        ],
        "answer": "C",
        "explanation": "Car is a type of Vehicle, so Car extends Vehicle."
    },
    {
        "type": "mcq",
        "question": "Which class would be the most appropriate superclass for the classes Student, Professor, and Secretary?",
        "options": [
            "Employee",
            "TeachingAssistant",
            "Person",
            "DepartmentChair",
            "Janitor"
        ],
        "answer": "C",
        "explanation": "Person is the most general class that encompasses Student, Professor, and Secretary."
    },
    {
        "type": "mcq",
        "question": "Which of the following 'instanceof' checks returns false for 'System.out' in Java?",
        "options": [
            "System.out instanceof PrintStream",
            "System.out instanceof OutputStream",
            "System.out instanceof Object",
            "System.out instanceof Closeable",
            "System.out instanceof Writer"
        ],
        "answer": "E",
        "explanation": "System.out is not an instance of Writer."
    },
    {
        "type": "mcq",
        "question": "Suppose class C implements interfaces I and J. Given the declarations:\n\nC c = ...;\nI i = ...;\nJ j = ...;\n\nWhich of the following assignments requires an explicit cast in Java?",
        "options": [
            "c = i;",
            "j = c;",
            "i = j;",
            "i = c;",
            "j = (J) c;"
        ],
        "answer": "A",
        "explanation": "Assigning from an interface type to a class type requires an explicit cast."
    },
    {
        "type": "mcq",
        "question": "Given the declarations:\n\nSandwich sub = new Sandwich();\nRectangle cerealBox = new Rectangle(5, 10, 20, 30);\nEdible e = null;\n\nWhich of the following assignment statements is legal in Java?",
        "options": [
            "e = sub;",
            "sub = e;",
            "sub = (Sandwich) cerealBox;",
            "e = (Edible) cerealBox;",
            "e = (Rectangle) cerealBox;"
        ],
        "answer": "A",
        "explanation": "Since Sandwich implements Edible, assigning 'sub' to 'e' is legal."
    },
    {
        "type": "mcq",
        "question": "If 'int a = 2000000000;' and 'int b = a;', what is the result of 'a - b'?",
        "options": [
            "0",
            "4000000000",
            "-4000000000",
            "Undefined behavior",
            "Compilation error"
        ],
        "answer": "A",
        "explanation": "Since 'a' equals 'b', 'a - b' equals 0."
    },
    {
        "type": "mcq",
        "question": "What is the result of 'Integer.compare(a, b);' given 'int a = 2000000000;' and 'int b = a;'?",
        "options": [
            "-1",
            "0",
            "1",
            "Compilation error",
            "Undefined behavior"
        ],
        "answer": "B",
        "explanation": "Since 'a' equals 'b', 'Integer.compare(a, b)' returns 0."
    },
    {
        "type": "mcq",
        "question": "How can you add a counter to a Java GUI program to count how many times a JButton has been clicked? Where should the counter be updated?",
        "options": [
            "By declaring a local variable inside the actionPerformed method; update it there.",
            "By declaring an instance variable in the class; update it inside the actionPerformed method.",
            "By using a static variable inside the actionPerformed method; update it there.",
            "By using a local variable inside the main method; update it inside the actionPerformed method.",
            "By declaring a variable inside the constructor; update it inside the paintComponent method."
        ],
        "answer": "B",
        "explanation": "An instance variable in the class retains its value across method calls and can be updated in the actionPerformed method each time the button is clicked."
    },
    {
        "type": "mcq",
        "question": "Why are inner classes often used for event listeners in Java GUI programming?",
        "options": [
            "Because they are required by the Java language for event handling.",
            "To allow the event listener to access private members of the outer class.",
            "Because inner classes execute faster than top-level classes.",
            "To keep the code organized in separate files.",
            "Because event listeners cannot be implemented as top-level classes."
        ],
        "answer": "B",
        "explanation": "Inner classes have access to the private fields and methods of the outer class, which is useful for event handling."
    },
    {
        "type": "mcq",
        "question": "Is it necessary to use inheritance to create JFrame instances in Java Swing applications?",
        "options": [
            "Yes, you must always extend JFrame to create a window.",
            "No, you can create a JFrame instance without extending it.",
            "Yes, inheritance is required for all Swing components.",
            "No, you should use JWindow instead of JFrame.",
            "Yes, but only if you override the paint method."
        ],
        "answer": "B",
        "explanation": "You can create a JFrame by instantiating it directly without extending it."
    },
    {
        "type": "mcq",
        "question": "Which of the following best describes the difference between a JLabel, a JTextField, and a JTextArea in Java Swing?",
        "options": [
            "JLabel is for displaying images, JTextField and JTextArea are for text input.",
            "JLabel and JTextField are single-line, JTextArea can display multiple lines.",
            "JLabel can be edited by the user, JTextField and JTextArea cannot.",
            "JTextField and JTextArea are for output, JLabel is for input.",
            "All three components are functionally identical."
        ],
        "answer": "B",
        "explanation": "JLabel and JTextField typically display single lines; JTextArea can display and accept multiple lines of text."
    },
    {
        "type": "mcq",
        "question": "Which method is declared in JTextArea but not inherited from JTextComponent?",
        "options": [
            "append(String str)",
            "getText()",
            "setEditable(boolean b)",
            "setText(String t)",
            "copy()"
        ],
        "answer": "A",
        "explanation": "The append(String str) method is specific to JTextArea and allows appending text."
    },
    {
        "type": "mcq",
        "question": "Who calls the paintComponent method of a Swing component, and when does this call occur?",
        "options": [
            "The programmer calls it directly when needed.",
            "The Swing framework calls it when the component needs to be repainted.",
            "It is called automatically at regular time intervals.",
            "The operating system calls it during application startup.",
            "It is never called; paintComponent is deprecated."
        ],
        "answer": "B",
        "explanation": "The Swing framework calls paintComponent when the component needs redrawing."
    },
    {
        "type": "mcq",
        "question": "In a custom Swing component, why might you draw an oval before drawing a string in the paintComponent method?",
        "options": [
            "Because the last drawing operation appears on top of previous ones.",
            "Because drawing order does not affect rendering.",
            "To improve performance.",
            "Because strings cannot be drawn over shapes.",
            "To ensure the shapes are hidden behind text."
        ],
        "answer": "A",
        "explanation": "Drawing operations are layered; drawing the string last ensures it appears on top."
    },
    {
        "type": "mcq",
        "question": "How would you specify a custom text color when drawing a string in the paintComponent method?",
        "options": [
            "By setting the foreground color of the component.",
            "By calling setColor(Color c) on the Graphics object before drawing.",
            "By using HTML tags within the string.",
            "By changing the background color of the component.",
            "By overriding the default font."
        ],
        "answer": "B",
        "explanation": "You set the color by calling g.setColor(Color c) before g.drawString()."
    },
    {
        "type": "mcq",
        "question": "What is the primary difference between the methods paintComponent(Graphics g) and repaint() in Java Swing?",
        "options": [
            "paintComponent schedules a repaint; repaint performs the painting immediately.",
            "repaint schedules a call to paintComponent; paintComponent contains the code to actually render the component.",
            "They are different names for the same method.",
            "paintComponent is used for components; repaint is used for containers.",
            "repaint() is called by the programmer; paintComponent() cannot be called directly."
        ],
        "answer": "B",
        "explanation": "repaint() schedules a repaint event, which leads to paintComponent being called by the Swing framework."
    },
    {
        "type": "mcq",
        "question": "Given the method call getWidth() inside the paintComponent method of a Swing component, why does this call not require an explicit parameter?",
        "options": [
            "Because getWidth() is a static method.",
            "Because it is an inherited method and can be called directly.",
            "Because paintComponent is a method of the component, and getWidth() is called on 'this'.",
            "Because getWidth() is a method of the Graphics object passed to paintComponent.",
            "Because Java allows methods to be called without specifying the object."
        ],
        "answer": "C",
        "explanation": "Within an instance method, methods of the current object can be called directly; 'this' is implied."
    },
    {
        "type": "mcq",
        "question": "How would you add a counter to a Java GUI program that prints how often a JButton has been clicked? Where is the counter updated?",
        "options": [
            "Declare a local variable inside the actionPerformed method; update it there.",
            "Declare an instance variable in the class; update it inside the actionPerformed method.",
            "Use a static variable inside the actionPerformed method; update it there.",
            "Declare a local variable inside the main method; update it there.",
            "Use a global variable outside all classes; update it inside the actionPerformed method."
        ],
        "answer": "B",
        "explanation": "An instance variable retains its value between method calls and can be updated each time the button is clicked inside the actionPerformed method."
    },
    {
        "type": "mcq",
        "question": "How would you add a counter to a Java GUI program that shows how often a JButton has been clicked? Where is the counter updated and displayed?",
        "options": [
            "Update and display the counter inside the actionPerformed method using a local variable.",
            "Update the counter inside the actionPerformed method; display it using a JLabel.",
            "Use a static variable to update the counter; display it in the console.",
            "Update the counter in the main method; display it in a JOptionPane.",
            "Update and display the counter inside the paintComponent method."
        ],
        "answer": "B",
        "explanation": "The counter is updated in the actionPerformed method and displayed using a JLabel or similar component in the GUI."
    },
    {
        "type": "mcq",
        "question": "If Java did not have inner classes, could we still implement event listeners? How?",
        "options": [
            "No, inner classes are required for event listeners.",
            "Yes, by using anonymous classes.",
            "Yes, by implementing event listeners as separate top-level classes.",
            "No, event handling would not be possible without inner classes.",
            "Yes, but only by modifying the Java language."
        ],
        "answer": "C",
        "explanation": "Event listeners can be implemented as separate top-level classes that implement the necessary listener interfaces."
    },
    {
        "type": "mcq",
        "question": "Is it a requirement to use inheritance for JFrame as described in Java Swing programming?",
        "options": [
            "Yes, you must extend JFrame to create custom windows.",
            "No, you can instantiate JFrame directly without extending it.",
            "Yes, because JFrame is an abstract class.",
            "No, you should use JPanel instead of extending JFrame.",
            "Yes, inheritance is required for all GUI components."
        ],
        "answer": "B",
        "explanation": "You can create a JFrame by instantiating it directly and adding components to it; extending JFrame is optional."
    },
    {
        "type": "mcq",
        "question": "What is the difference between a JLabel, a JTextField, and a JTextArea in Java Swing?",
        "options": [
            "JLabel displays text, JTextField allows single-line text input, JTextArea allows multi-line text input.",
            "JLabel allows single-line text input, JTextField displays text, JTextArea allows multi-line text input.",
            "JLabel and JTextField are for images, JTextArea is for text input.",
            "JLabel and JTextArea are editable, JTextField is not.",
            "There is no difference; all are used for text display."
        ],
        "answer": "A",
        "explanation": "JLabel is used for displaying text or images, JTextField allows for single-line text input, and JTextArea allows for multi-line text input."
    },
    {
        "type": "mcq",
        "question": "Name a method that is declared in JTextArea, a method that JTextArea inherits from JTextComponent, and a method that JTextArea inherits from JComponent.",
        "options": [
            "Declared in JTextArea: append(); Inherited from JTextComponent: getText(); Inherited from JComponent: repaint()",
            "Declared in JTextArea: getText(); Inherited from JTextComponent: append(); Inherited from JComponent: isEditable()",
            "Declared in JTextArea: setSize(); Inherited from JTextComponent: append(); Inherited from JComponent: getText()",
            "Declared in JTextArea: isEditable(); Inherited from JTextComponent: setText(); Inherited from JComponent: append()",
            "Declared in JTextArea: repaint(); Inherited from JTextComponent: setText(); Inherited from JComponent: append()"
        ],
        "answer": "A",
        "explanation": "The append() method is declared in JTextArea; getText() is inherited from JTextComponent; repaint() is inherited from JComponent."
    },
    {
        "type": "mcq",
        "question": "Why did the program use a JTextArea and not a JLabel to show how the interest accumulates? How could you have achieved a similar effect with an array of labels?",
        "options": [
            "Because JTextArea supports multiple lines of text, whereas JLabel does not; you could use an array of JLabels to display multiple lines.",
            "Because JLabel cannot display text; using images would be necessary.",
            "Because JTextArea is more efficient than JLabel; you cannot achieve the same effect with JLabels.",
            "Because JLabel is deprecated; using JTextArea is mandatory.",
            "Because JTextArea automatically formats the text; JLabel cannot."
        ],
        "answer": "A",
        "explanation": "JTextArea allows for displaying multiple lines of text, which is suitable for accumulating interest outputs. Alternatively, an array of JLabels could be used to display each line individually."
    },
    {
        "type": "mcq",
        "question": "Who calls the paintComponent method of a component? When does the call to the paintComponent method occur?",
        "options": [
            "The programmer manually calls paintComponent when needed.",
            "The Swing framework calls paintComponent when the component needs to be redrawn.",
            "The paintComponent method is called automatically at fixed time intervals.",
            "The operating system calls paintComponent during system updates.",
            "It is called only once when the component is created."
        ],
        "answer": "B",
        "explanation": "The Swing framework automatically calls paintComponent when it determines that the component needs to be redrawn, such as when it is first shown or when repaint() is invoked."
    },
    {
        "type": "mcq",
        "question": "In a drawing routine, why was the oval drawn before the string?",
        "options": [
            "Because drawing operations are layered; the last item drawn appears on top.",
            "Because ovals must always be drawn before text in Java.",
            "Because strings cannot overlap shapes.",
            "Because the order of drawing does not affect the output.",
            "Because ovals render faster when drawn first."
        ],
        "answer": "A",
        "explanation": "In graphics rendering, items drawn later are displayed over items drawn earlier. Drawing the string after the oval ensures the text appears on top of the oval."
    },
    {
        "type": "mcq",
        "question": "How do you specify a text color when drawing in the paintComponent method?",
        "options": [
            "By calling setColor(Color c) on the Graphics object before drawing the text.",
            "By setting the foreground color of the component.",
            "By using HTML tags in the string.",
            "By setting the background color before drawing.",
            "By changing the system theme."
        ],
        "answer": "A",
        "explanation": "You specify the drawing color by calling g.setColor(Color c) on the Graphics object before performing any drawing operations like g.drawString()."
    },
    {
        "type": "mcq",
        "question": "What is the difference between the paintComponent and repaint methods?",
        "options": [
            "paintComponent schedules a repaint; repaint performs the painting.",
            "repaint schedules a call to paintComponent; paintComponent contains the code to render the component.",
            "They are the same method with different names.",
            "repaint is used for printing; paintComponent is used for screen rendering.",
            "paintComponent is called by the programmer; repaint is called by the system."
        ],
        "answer": "B",
        "explanation": "The repaint() method schedules a repaint event in the event queue, causing the Swing framework to invoke paintComponent(), where the actual drawing code resides."
    },
    {
        "type": "mcq",
        "question": "Explain why the call to the getWidth method in the ChartComponent class has no explicit parameter.",
        "options": [
            "Because getWidth is a static method.",
            "Because getWidth is an instance method implicitly called on 'this'.",
            "Because getWidth is a private method.",
            "Because getWidth does not require any parameters by definition.",
            "Because getWidth is inherited and cannot be called with a parameter."
        ],
        "answer": "B",
        "explanation": "Within an instance method like paintComponent, calling getWidth() without a receiver automatically refers to 'this.getWidth()'."
    },
    {
        "type": "mcq",
        "question": "Which relationship is appropriate between the classes University and Student?",
        "options": [
            "Inheritance",
            "Aggregation",
            "Association",
            "Implementation",
            "Dependency"
        ],
        "answer": "B",
        "explanation": "Aggregation is appropriate because a University is composed of Students."
    },
    {
        "type": "mcq",
        "question": "Considering the classes Student and TeachingAssistant, what relationship is appropriate?",
        "options": [
            "Student extends TeachingAssistant",
            "TeachingAssistant extends Student",
            "No relationship",
            "Both inherit from Person",
            "TeachingAssistant implements Student"
        ],
        "answer": "B",
        "explanation": "A TeachingAssistant is a specialized Student, so TeachingAssistant extends Student."
    },
    {
        "type": "mcq",
        "question": "Between the classes Student and Freshman, which inheritance relationship is correct?",
        "options": [
            "Student extends Freshman",
            "Freshman extends Student",
            "They are unrelated",
            "Both inherit from Person",
            "Freshman implements Student"
        ],
        "answer": "B",
        "explanation": "A Freshman is a specific type of Student, so Freshman extends Student."
    },
    {
        "type": "mcq",
        "question": "Which relationship is appropriate between the classes Car and Door?",
        "options": [
            "Inheritance",
            "Aggregation",
            "Implementation",
            "No relationship",
            "Dependency"
        ],
        "answer": "B",
        "explanation": "A Car is composed of Doors; thus, the relationship is aggregation."
    },
    {
        "type": "mcq",
        "question": "Given that Truck is a type of Vehicle, which relationship is appropriate?",
        "options": [
            "Truck extends Vehicle",
            "Vehicle extends Truck",
            "Truck implements Vehicle",
            "Vehicle implements Truck",
            "No relationship"
        ],
        "answer": "A",
        "explanation": "Truck is a specialized Vehicle, so Truck extends Vehicle."
    },
    {
        "type": "mcq",
        "question": "In the context of object-oriented design, should the class BMW inherit from the class Vehicle?",
        "options": [
            "Yes, because every BMW is a Vehicle",
            "No, because BMW is a manufacturer, not a Vehicle",
            "Yes, because BMW produces Vehicles",
            "No, BMW should implement Vehicle",
            "It depends on the design"
        ],
        "answer": "B",
        "explanation": "BMW is a manufacturer, so it should not inherit from Vehicle."
    },
    {
        "type": "mcq",
        "question": "Why is it not a good idea for the class Circle to inherit from the class Point?",
        "options": [
            "Because Circle and Point are unrelated",
            "Because Circle is not a type of Point",
            "Because Circle should inherit from Shape instead",
            "Because inheritance would violate encapsulation",
            "Because Point should inherit from Circle"
        ],
        "answer": "B",
        "explanation": "A Circle is not a Point; rather, it may have a Point as its center."
    },
    {
        "type": "mcq",
        "question": "Which of the following best describes an aggregation relationship?",
        "options": [
            "A class inherits from another class",
            "A class contains objects of another class",
            "A class depends on another class",
            "A class overrides methods of another class",
            "A class implements an interface"
        ],
        "answer": "B",
        "explanation": "Aggregation represents a whole-part relationship where one class contains objects of another."
    },
    {
        "type": "mcq",
        "question": "Given a class Rectangle with instance variables width and height, which of the following is a correct recursive method to calculate the area?",
        "options": [
            "public int getArea() { return width * height; }",
            "public int getArea() { return getArea(width - 1, height - 1); }",
            "public int getArea() { if (width == 0) return 0; else return height + new Rectangle(width - 1, height).getArea(); }",
            "public int getArea() { return width + new Rectangle(width, height - 1).getArea(); }",
            "public int getArea() { return width + height; }"
        ],
        "answer": "C",
        "explanation": "This method recursively reduces the width until it reaches zero, summing up the height each time."
    },
    {
        "type": "mcq",
        "question": "Which of the following recursive methods correctly reverses a string in Java?",
        "options": [
            "public String reverse(String text) { return new StringBuilder(text).reverse().toString(); }",
            "public String reverse(String text) { if (text.isEmpty()) return text; else return reverse(text.substring(1)) + text.charAt(0); }",
            "public String reverse(String text) { return text; }",
            "public String reverse(String text) { return reverse(text.substring(0, text.length() - 1)); }",
            "public String reverse(String text) { return text.charAt(text.length() - 1) + reverse(text.substring(0, text.length() - 1)); }"
        ],
        "answer": "B",
        "explanation": "Option B correctly uses recursion by calling reverse on the substring excluding the first character and appending the first character at the end."
    },
    {
        "type": "mcq",
        "question": "What is the base case in the following recursive method for computing the sum of an integer array?\n\n```java\npublic int sum(int[] array, int n) {\n    if (n <= 0) return 0;\n    else return sum(array, n - 1) + array[n - 1];\n}\n```",
        "options": [
            "When n == array.length",
            "When n == 0",
            "When n == 1",
            "When array[n] == 0",
            "When sum == 0"
        ],
        "answer": "B",
        "explanation": "The base case occurs when n is 0, at which point the method returns 0."
    },
    {
        "type": "mcq",
        "question": "Which statement best describes tail recursion?",
        "options": [
            "A recursive function that has multiple recursive calls.",
            "A recursive function where the recursive call is the last operation in the function.",
            "A function that calls itself at the start of its execution.",
            "A recursive function that does not have a base case.",
            "A recursive function that increases the problem size with each call."
        ],
        "answer": "B",
        "explanation": "Tail recursion occurs when the recursive call is the final action in the function."
    },
    {
        "type": "mcq",
        "question": "Given the following recursive method:\n\n```java\npublic int factorial(int n) {\n    if (n == 0) return 1;\n    else return n * factorial(n - 1);\n}\n```\nWhat is the value of factorial(5)?",
        "options": [
            "120",
            "24",
            "60",
            "720",
            "None of the above"
        ],
        "answer": "A",
        "explanation": "factorial(5) = 5 * 4 * 3 * 2 * 1 = 120."
    },
    {
        "type": "mcq",
        "question": "How many times is the fib method called when computing fib(5) using the naive recursive Fibonacci implementation?\n\n```java\npublic int fib(int n) {\n    if (n <= 1) return n;\n    else return fib(n - 1) + fib(n - 2);\n}\n```",
        "options": [
            "5",
            "7",
            "9",
            "15",
            "None of the above"
        ],
        "answer": "D",
        "explanation": "The method is called 15 times due to overlapping subproblems in the recursive calls."
    },
    {
        "type": "mcq",
        "question": "Which of the following problems is most efficiently solved using recursion?",
        "options": [
            "Calculating the sum of a list of numbers",
            "Finding the maximum element in an array",
            "Traversal of a binary tree",
            "Calculating the average of numbers",
            "Sorting an array using bubble sort"
        ],
        "answer": "C",
        "explanation": "Binary tree traversal is naturally recursive and efficiently implemented using recursion."
    },
    {
        "type": "mcq",
        "question": "What does the following recursive method compute?\n\n```java\npublic int mystery(int n) {\n    if (n == 0) return 0;\n    else return n + mystery(n - 1);\n}\n```",
        "options": [
            "Factorial of n",
            "n squared",
            "Sum of numbers from 0 to n",
            "n times n minus 1",
            "Always returns 0"
        ],
        "answer": "C",
        "explanation": "The method computes the sum of all integers from n down to 1."
    },
    {
        "type": "mcq",
        "question": "Given a recursive method to compute the greatest common divisor (GCD) of two numbers:\n\n```java\npublic int gcd(int a, int b) {\n    if (b == 0) return a;\n    else return gcd(b, a % b);\n}\n```\nWhat is gcd(48, 18)?",
        "options": [
            "6",
            "12",
            "18",
            "48",
            "3"
        ],
        "answer": "A",
        "explanation": "gcd(48, 18) computes to 6 using the Euclidean algorithm."
    },
    {
        "type": "mcq",
        "question": "Which of the following statements about recursion is FALSE?",
        "options": [
            "Every recursive method must have a base case.",
            "Recursion can sometimes be replaced with iteration.",
            "Recursive methods always use less memory than iterative methods.",
            "Recursion involves a method calling itself.",
            "Recursive solutions are often more elegant for problems like tree traversal."
        ],
        "answer": "C",
        "explanation": "Recursive methods can use more memory due to the call stack overhead."
    },
    {
        "type": "mcq",
        "question": "Given an algorithm that runs in O(n) time, if it takes 5 seconds to process 1,000 records, approximately how long will it take to process 2,000 records?",
        "options": [
            "5 seconds",
            "10 seconds",
            "15 seconds",
            "20 seconds",
            "25 seconds"
        ],
        "answer": "B",
        "explanation": "For an O(n) algorithm, doubling the input size doubles the processing time. So, it will take approximately 10 seconds."
    },
    {
        "type": "mcq",
        "question": "Which of the following growth rates has the slowest rate of increase?",
        "options": [
            "O(log n)",
            "O(n)",
            "O(n log n)",
            "O(n^2)",
            "O(2^n)"
        ],
        "answer": "A",
        "explanation": "O(log n) grows the slowest among the listed options."
    },
    {
        "type": "mcq",
        "question": "What is the big-O time complexity of reversing an array using the following method?\n\n```java\npublic static void swap(int[] a) {\n    int i = 0;\n    int j = a.length - 1;\n    while (i < j) {\n        int temp = a[i];\n        a[i] = a[j];\n        a[j] = temp;\n        i++;\n        j--;\n    }\n}\n```",
        "options": [
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n log n)",
            "O(n^2)"
        ],
        "answer": "C",
        "explanation": "The method swaps elements from both ends towards the center, resulting in O(n) time complexity."
    },
    {
        "type": "mcq",
        "question": "Which sorting algorithm has the best time complexity for large datasets with random data?",
        "options": [
            "Bubble Sort",
            "Merge Sort",
            "Insertion Sort",
            "Selection Sort",
            "Quick Sort"
        ],
        "answer": "E",
        "explanation": "Quick Sort has an average time complexity of O(n log n) and performs well on large random datasets."
    },
    {
        "type": "mcq",
        "question": "What is the big-O time complexity of finding the most frequent element in an unsorted array using a hashmap?",
        "options": [
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n log n)",
            "O(n^2)"
        ],
        "answer": "C",
        "explanation": "Using a hashmap to count frequencies requires a single pass through the array, resulting in O(n) time."
    },
    {
        "type": "mcq",
        "question": "If an algorithm has a time complexity of O(n log n), which of the following could be an example?",
        "options": [
            "Binary Search",
            "Merge Sort",
            "Linear Search",
            "Bubble Sort",
            "Calculating Fibonacci numbers recursively"
        ],
        "answer": "B",
        "explanation": "Merge Sort is a classic example of an O(n log n) time complexity algorithm."
    },
    {
        "type": "mcq",
        "question": "What is the time complexity of removing duplicates from an unsorted array by first sorting it and then removing consecutive duplicates?",
        "options": [
            "O(n)",
            "O(n log n)",
            "O(n^2)",
            "O(log n)",
            "O(n^2 log n)"
        ],
        "answer": "B",
        "explanation": "Sorting the array takes O(n log n) time, and removing duplicates in a single pass after sorting takes O(n), so the overall time is O(n log n)."
    },
    {
        "type": "mcq",
        "question": "Which of the following sorting algorithms is stable?",
        "options": [
            "Selection Sort",
            "Quick Sort",
            "Insertion Sort",
            "Heap Sort",
            "None of the above"
        ],
        "answer": "C",
        "explanation": "Insertion Sort is stable because it does not change the relative order of equal elements."
    },
    {
        "type": "mcq",
        "question": "What is the time complexity of Bubble Sort in the worst case?",
        "options": [
            "O(n)",
            "O(n log n)",
            "O(n^2)",
            "O(log n)",
            "O(n^3)"
        ],
        "answer": "C",
        "explanation": "In the worst case, Bubble Sort performs O(n^2) comparisons and swaps."
    },
    {
        "type": "mcq",
        "question": "Which sorting algorithm can achieve O(n) time complexity under certain conditions, such as when the range of input data is known and limited?",
        "options": [
            "Merge Sort",
            "Quick Sort",
            "Heap Sort",
            "Radix Sort",
            "Insertion Sort"
        ],
        "answer": "D",
        "explanation": "Radix Sort can achieve O(n) time complexity when sorting integers with a fixed number of digits."
    },
    {
        "type": "mcq",
        "question": "Which method in the Collection interface can be used to perform a union of two sets in Java?",
        "options": [
            "addAll",
            "retainAll",
            "removeAll",
            "containsAll",
            "equals"
        ],
        "answer": "A",
        "explanation": "The addAll method adds all elements from one collection to another, effectively performing a union of two sets."
    },
    {
        "type": "mcq",
        "question": "What is the output of the following code snippet?\n\n```java\nLinkedList<String> list = new LinkedList<>();\nlist.addFirst(\"Alice\");\nlist.addLast(\"Bob\");\nlist.addFirst(\"Carol\");\nSystem.out.println(list.removeLast());\nSystem.out.println(list.removeFirst());\nSystem.out.println(list.remove());\n```\n",
        "options": [
            "Bob, Alice, Carol",
            "Bob, Carol, Alice",
            "Alice, Bob, Carol",
            "Carol, Bob, Alice",
            "Compilation error"
        ],
        "answer": "A",
        "explanation": "The list after additions is [Carol, Alice, Bob]. removeLast() removes 'Bob', removeFirst() removes 'Carol', remove() without index removes first element 'Alice'."
    },
    {
        "type": "mcq",
        "question": "Which of the following statements is TRUE regarding linked lists compared to array lists in Java?",
        "options": [
            "Linked lists offer faster random access than array lists.",
            "Linked lists have faster insertion and deletion at arbitrary positions than array lists.",
            "Linked lists consume less memory than array lists.",
            "Linked lists are thread-safe by default, unlike array lists.",
            "Linked lists do not support iterators."
        ],
        "answer": "B",
        "explanation": "Linked lists allow faster insertion and deletion at arbitrary positions because they only need to update the links, whereas array lists may require shifting elements."
    },
    {
        "type": "mcq",
        "question": "Which data structure is most appropriate for a deck of cards where cards are drawn from the top and returned to the bottom?",
        "options": [
            "Stack",
            "Queue",
            "PriorityQueue",
            "Set",
            "Map"
        ],
        "answer": "B",
        "explanation": "A queue is the appropriate data structure as it follows FIFO (First-In, First-Out), matching the behavior of drawing from the top and adding to the bottom."
    },
    {
        "type": "mcq",
        "question": "What is the main difference between a Set and a Map in Java?",
        "options": [
            "A Set stores unique keys with associated values; a Map stores values only.",
            "A Set allows duplicate elements; a Map does not.",
            "A Set stores unique elements; a Map stores key-value pairs.",
            "A Set maintains insertion order; a Map does not.",
            "There is no difference; Set and Map are the same."
        ],
        "answer": "C",
        "explanation": "A Set stores unique elements without duplicates, whereas a Map stores key-value pairs."
    },
    {
        "type": "mcq",
        "question": "Which method can be used to compute the intersection of two sets in Java?",
        "options": [
            "setA.addAll(setB);",
            "setA.removeAll(setB);",
            "setA.retainAll(setB);",
            "setA.containsAll(setB);",
            "setA.equals(setB);"
        ],
        "answer": "C",
        "explanation": "The retainAll method retains only the elements in setA that are also contained in setB, resulting in the intersection."
    },
    {
        "type": "mcq",
        "question": "Can a Java Map have two keys with the same value and two values with the same key?",
        "options": [
            "Yes to both",
            "No to both",
            "Yes to same keys with same value only",
            "Yes to same values with different keys only",
            "No, each key-value pair must be unique"
        ],
        "answer": "D",
        "explanation": "In a Map, keys must be unique, but values can be duplicated. So, two keys can have the same value, but a key cannot have multiple values."
    },
    {
        "type": "mcq",
        "question": "How can you remove all elements of a LinkedList<String> that have length less than 4?",
        "options": [
            "Using a for loop and remove(index);",
            "Using iterator.removeIf(s -> s.length() < 4);",
            "Using list.removeIf(s -> s.length() < 4);",
            "Using list.deleteIf(s -> s.length() < 4);",
            "Using list.removeAll(s -> s.length() < 4);"
        ],
        "answer": "C",
        "explanation": "The removeIf method can be used with a lambda expression to remove elements based on a condition."
    },
    {
        "type": "mcq",
        "question": "Which of the following code snippets correctly prints all key-value pairs of a Map<String, Integer> map?",
        "options": [
            "for (String key : map.keySet()) { System.out.println(key + \": \" + map.get(key)); }",
            "for (Map.Entry<String, Integer> entry : map.entrySet()) { System.out.println(entry); }",
            "map.forEach((k, v) -> System.out.println(k + \": \" + v));",
            "All of the above",
            "None of the above"
        ],
        "answer": "D",
        "explanation": "All the provided code snippets correctly iterate over the map's entries and print them."
    },
    {
        "type": "mcq",
        "question": "Which of the following is TRUE about Java's hashCode method in the Object class?",
        "options": [
            "It returns a unique integer for every object.",
            "Equal objects must have equal hash codes.",
            "It cannot be overridden.",
            "It is used only in cryptographic hashing.",
            "It guarantees the distribution of hash codes."
        ],
        "answer": "B",
        "explanation": "According to Java's contract, if two objects are equal according to the equals() method, they must have the same hash code."
    },
    {
        "type": "mcq",
        "question": "What is the time complexity of accessing the k-th element in a singly-linked list with n elements?",
        "options": [
            "O(1)",
            "O(log n)",
            "O(k)",
            "O(n)",
            "O(n^2)"
        ],
        "answer": "D",
        "explanation": "Accessing the k-th element requires traversing from the head to the k-th node, resulting in O(n) time in the worst case."
    },
    {
        "type": "mcq",
        "question": "Why is it unsafe to remove the first element of a linked list when an iterator has just traversed it?",
        "options": [
            "It can cause a NullPointerException.",
            "It may invalidate the iterator's state, leading to incorrect behavior.",
            "Because the first element cannot be removed during iteration.",
            "It automatically removes all elements in the list.",
            "The iterator will skip the next element."
        ],
        "answer": "B",
        "explanation": "Removing the first element can invalidate the iterator's current position, causing unexpected behavior during iteration."
    },
    {
        "type": "mcq",
        "question": "What is the big-O efficiency of the following loop, given that myList is a linked list with size() implemented by counting nodes, and get(i) traverses from the head?\n\n```java\nfor (int i = 0; i < myList.size(); i++) {\n    System.out.println(myList.get(i));\n}\n```",
        "options": [
            "O(n)",
            "O(n log n)",
            "O(n^2)",
            "O(log n)",
            "O(1)"
        ],
        "answer": "C",
        "explanation": "Each call to get(i) takes O(n) time, and it's called n times, resulting in O(n^2) complexity."
    },
    {
        "type": "mcq",
        "question": "In a doubly-linked list of length n, why doesn't starting from the end when k > n/2 improve the big-O efficiency of element access?",
        "options": [
            "Because starting from the end is less efficient.",
            "Because big-O notation ignores constant factors.",
            "Because the average case remains O(n).",
            "Because accessing elements still requires O(n) time.",
            "Because it only improves the best-case scenario."
        ],
        "answer": "D",
        "explanation": "Even by starting from the end, accessing an element by index in a doubly-linked list remains O(n) in big-O terms."
    },
    {
        "type": "mcq",
        "question": "Which data structure allows O(1) time complexity for addFirst, removeFirst, addLast, and removeLast operations?",
        "options": [
            "Singly-linked list",
            "Doubly-linked list",
            "Circular array",
            "All of the above",
            "None of the above"
        ],
        "answer": "D",
        "explanation": "Both doubly-linked lists and circular arrays can implement a deque with O(1) time for operations at both ends."
    },
    {
        "type": "mcq",
        "question": "How can you implement a queue using two stacks?",
        "options": [
            "By using one stack for enqueue and one stack for dequeue operations.",
            "By alternating stack operations for each element.",
            "It's not possible to implement a queue with stacks.",
            "By reversing the stack after each operation.",
            "By using recursion within the stack."
        ],
        "answer": "A",
        "explanation": "Using two stacks—one for incoming elements and one for outgoing—can simulate queue behavior."
    },
    {
        "type": "mcq",
        "question": "What problem arises when modifying a linked list using two iterators simultaneously?",
        "options": [
            "It leads to data duplication.",
            "Iterators cannot function with simultaneous modifications.",
            "It can cause incorrect results due to iterator state corruption.",
            "It enhances performance unpredictably.",
            "No problem arises; it's perfectly safe."
        ],
        "answer": "C",
        "explanation": "Simultaneous modifications can corrupt the internal state of iterators, causing incorrect behavior."
    },
    {
        "type": "mcq",
        "question": "Why might a linked list implementation throw a ConcurrentModificationException?",
        "options": [
            "Because the list size exceeds its capacity.",
            "Due to multiple threads accessing the list.",
            "When the list detects that it has been modified structurally during iteration.",
            "If an unsupported operation is called.",
            "When elements are removed excessively."
        ],
        "answer": "C",
        "explanation": "A ConcurrentModificationException is thrown if the list is structurally modified outside of the iterator during iteration."
    },
    {
        "type": "mcq",
        "question": "What is the disadvantage of enhancing a linked list with an array of references to every tenth node to improve get(i) performance?",
        "options": [
            "It increases the time complexity of get(i) to O(n^2).",
            "It consumes additional memory proportional to n.",
            "It makes insertion and deletion operations less efficient.",
            "It complicates the implementation without any benefit.",
            "It breaches the principles of linked lists."
        ],
        "answer": "B",
        "explanation": "Storing references to every tenth node uses extra memory, increasing space complexity."
    },
    {
        "type": "mcq",
        "question": "Why is assigning a unique ID to each object not a suitable replacement for implementing a proper hash function in a hash table?",
        "options": [
            "Unique IDs cannot be generated efficiently.",
            "Unique IDs do not guarantee an even distribution in the hash table.",
            "It violates the hash table implementation.",
            "Because objects can share the same unique ID.",
            "Unique IDs are not supported in Java."
        ],
        "answer": "B",
        "explanation": "Using unique IDs may not distribute entries evenly across the hash table buckets, leading to poor performance."
    },
    {
        "type": "mcq",
        "question": "Which traversal method would print the nodes of a binary search tree in ascending order?",
        "options": [
            "Preorder traversal",
            "Inorder traversal",
            "Postorder traversal",
            "Level-order traversal",
            "Reverse inorder traversal"
        ],
        "answer": "B",
        "explanation": "Inorder traversal visits nodes in the order: left subtree, root, right subtree, resulting in nodes being printed in ascending order for binary search trees."
    },
    {
        "type": "mcq",
        "question": "What is the time complexity of checking whether two binary trees have the same shape?",
        "options": [
            "O(1)",
            "O(log n)",
            "O(n)",
            "O(n log n)",
            "O(n^2)"
        ],
        "answer": "C",
        "explanation": "You need to visit each node in both trees once to compare their structures, resulting in O(n) time complexity."
    },
    {
        "type": "mcq",
        "question": "In a red-black tree, which of the following properties must always be true?",
        "options": [
            "Every node is either red or black.",
            "No two red nodes can be adjacent.",
            "All paths from a node to its null descendants contain the same number of black nodes.",
            "The root is always black.",
            "All of the above."
        ],
        "answer": "E",
        "explanation": "All listed properties are defining characteristics of red-black trees."
    },
    {
        "type": "mcq",
        "question": "What is the maximum height of a red-black tree with n nodes?",
        "options": [
            "O(log n)",
            "O(n)",
            "O(n log n)",
            "O(sqrt n)",
            "O(1)"
        ],
        "answer": "A",
        "explanation": "Red-black trees have a height of at most 2 * log₂(n + 1), which is O(log n)."
    },
    {
        "type": "mcq",
        "question": "Which traversal method processes the root node after its subtrees?",
        "options": [
            "Inorder traversal",
            "Preorder traversal",
            "Postorder traversal",
            "Level-order traversal",
            "Reverse preorder traversal"
        ],
        "answer": "C",
        "explanation": "Postorder traversal visits the left subtree, then the right subtree, and processes the root node last."
    },
    {
        "type": "mcq",
        "question": "In a binary search tree, how is the node with the smallest value located?",
        "options": [
            "By traversing to the leftmost node",
            "By traversing to the rightmost node",
            "By performing a preorder traversal",
            "By checking the root node",
            "By using a hash function"
        ],
        "answer": "A",
        "explanation": "In a BST, the smallest value is found at the leftmost node."
    },
    {
        "type": "mcq",
        "question": "Which of the following is TRUE about heaps?",
        "options": [
            "Heaps are always balanced binary trees.",
            "In a max-heap, each parent node is greater than or equal to its child nodes.",
            "Heaps can be efficiently traversed in sorted order.",
            "Heaps are a type of binary search tree.",
            "Heap insertion and deletion have O(n) time complexity."
        ],
        "answer": "B",
        "explanation": "In a max-heap, the key at each node is greater than or equal to the keys of its children."
    },
    {
        "type": "mcq",
        "question": "Given a complete binary tree represented as an array starting at index 1, what is the parent index of the node at index i?",
        "options": [
            "i / 2",
            "2 * i",
            "2 * i + 1",
            "i - 1",
            "i + 1"
        ],
        "answer": "A",
        "explanation": "In an array-based heap, the parent of the node at index i is located at index floor(i / 2)."
    },
    {
        "type": "mcq",
        "question": "What is the minimum number of nodes in a red-black tree of black height bh?",
        "options": [
            "2^(bh) - 1",
            "2^(bh) + 1",
            "bh",
            "bh^2",
            "bh * log n"
        ],
        "answer": "A",
        "explanation": "A red-black tree with black height bh has at least 2^bh - 1 nodes."
    },
    {
        "type": "mcq",
        "question": "Which traversal method would you use to delete all nodes of a binary tree starting from the leaves up to the root?",
        "options": [
            "Inorder traversal",
            "Preorder traversal",
            "Postorder traversal",
            "Level-order traversal",
            "Random traversal"
        ],
        "answer": "C",
        "explanation": "Postorder traversal processes child nodes before their parents, making it suitable for safely deleting nodes."
    }
]