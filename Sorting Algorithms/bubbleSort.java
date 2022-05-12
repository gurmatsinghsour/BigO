import java.util.Scanner;

public class bubbleSort {

    static void bubbleSorting(int array[]) {
        for (int i = 0; i <= (array.length - 2); i++) {
            for (int j = 0; j <= (array.length - 2 - i); j++) {
                if (array[j] > array[j + 1]) {

                    int temp = array[j + 1];
                    array[j + 1] = array[j];
                    array[j] = temp;

                }
            }
        }

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of elements : ");
        int num = sc.nextInt();

        int[] array = new int[num];

        System.out.print("Enter the elements : ");
        for (int i = 0; i < num; i++) {
            array[i] = sc.nextInt();

        }
        bubbleSorting(array);

        for (int j = 0; j < array.length; j++) {
            System.out.print(array[j] + " ");
        }
    }

}

