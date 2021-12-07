public class bigOofNsquare {

    public static void main(String[] args) {

        int array1[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

        for (int i = 0; i < array1.length; i++) {
            for (int j = 1; j < array1.length; j++) {

                int finalno = i + j;
                System.out.println(finalno);

            }
        }

    }

}

// This program is the representation of O(n^2) as it's quadratic and there are
// two nested loops.