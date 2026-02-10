import java.util.Scanner;

class first {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        Float Price = sc.nextFloat();
        System.out.println("Hello "+name);
        
         
        System.out.println("your age is "+ a);
        System.out.println( "your age is "+ b);
        System.out.println("your age is " + c);
        System.out.println(a / b);
        System.out.println(b / c);
        System.out.println(a / c );
    }
 
}

