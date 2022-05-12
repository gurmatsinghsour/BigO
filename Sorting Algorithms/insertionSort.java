import  java.util.Scanner;
public class insertionSort {
    static void insertionSort (int array[]) {


        for(int i = 0; i<array.length-2; i++ ) {

            int currentValue = array[i];
            int j = i-1;
            while(j>=0 && array[j] > currentValue) {
                array[j+1] = array[j];
                j -= 1;
            }
            array[j+1] = currentValue;

        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of elements : ");
        int num = sc.nextInt();

        int array[] = new int[num];

        System.out.print("Enter the elements : ");
        for(int i=0; i<num; i++) {
            array[i] = sc.nextInt();
        }

        insertionSort(array);

        for (int j = 0; j < array.length; j++) {
            System.out.print(array[j] + " ");
        }
    }
}
