public class bigOofN {

    // In BigO we usually find the worst case scenario like in the below example
    static void Example() {

        String[] array2 = { "Arcy", "Sam", "Joe", "Wezol", "Lurid", "eren yaeger", "Levi" };

        // Let's say that you want to find if Levi exists in the above array and as you
        // can see it's at the end of the array and to find the levi it will have to
        // iterate over all --
        // -- elements in the array like first it'll check array2[0] then array2[1] etc
        // so here more the operations are performed in this programs and let's say Levi
        // is in the middle of the loop --
        // -- and i only want it to find it once but it's still gona find since it's
        // iterating over the length of the array so to fix that we'll use 'break' i
        // mean this is how we try to improve our code --
        // -- using Big O

        for (int i = 0; i < array2.length; i++) { // O(n)
            if (array2[i] == "Levi") {
                // Here we're gonna find Levi from the
                System.out.println("Found Levi!");
                break;
            } else {
                System.out.println("Not Found");
            }
        }

    }

    public static void main(String[] args) {

        System.out.println("______________Example 1________________");

        String[] array = { "Arcy", "Sam", "Joe" };

        for (int i = 0; i < array.length; i++) { // O(n)

            System.out.println(array[i]);
        }

        System.out.println("______________Example 2________________");

        Example();
    }
}

// This is the representation of O(n)