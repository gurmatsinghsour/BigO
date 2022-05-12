package pkg4;

public class LinkedListDemo {
    public static void main(String[] args) {
        LinkedList list = new LinkedList();

        list.insertAtHead(5);
        list.insertAtHead(10);
        list.insertAtHead(29);
        list.insertAtHead(13);
        list.insertAtHead(42);
        list.insertAtHead(59);
        list.insertAtHead(6);

        list.deleteHead();

        System.out.println(list);
        System.out.println("Length  " + list.length());
        System.out.println("Found " + list.search(59));


    }
}
