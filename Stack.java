public class Stack {
    public int[] list = new int[1];

    public static void main(String[] args) {
        Stack s = new Stack();
        s.push(1);
        s.push(3);
        s.push(2);
        System.out.println(s.toString());
    }

    public void push(int element) {
        if (list.length > 0) {
            int[] temp_list = new int[list.length];
            for (int i = 0; i < list.length; i++) {
                temp_list[i] = list[i];
            }
            int[] list = new int[temp_list.length + 1];
            for (int i = 0; i < temp_list.length; i++) {
                list[i] = temp_list[i];
            }
            list[temp_list.length + 1] = element;
        } else {
            list[0] = element;
        }
    }

    @Override
    public String toString() {
        String str = "";
        for (int i : list) {
            str += " " + i + " ";
        }
        return str;
    }
}
