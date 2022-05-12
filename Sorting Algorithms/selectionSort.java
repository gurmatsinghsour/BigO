import java.util.Scanner;

public class selectionSort {

    static void selectionSorting(int array[]) {

        for(int i=0; i<array.length-2; i++){
            int minIndex=  i;
            for(int j=i+1; j<array.length-1; j++){
                if (array[j] < array[minIndex]){
                    minIndex = j;

                }
            }
            int temp = array[minIndex];
            array[minIndex] = array[i];
            array[i] = temp;

        }

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the length of data : ");
        int num = sc.nextInt();

        int array[] = new int[num];

        for(int i = 0; i<num; i++){
            array[i] = sc.nextInt();
        }

        selectionSorting(array);
        for (int j = 0; j < array.length; j++) {
            System.out.print(array[j] + " ");
        }
    }
}
