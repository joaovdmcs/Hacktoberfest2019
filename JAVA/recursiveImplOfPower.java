import java.util.Scanner;

class Main {
  public static int potenciaRecursiva(int a, int b){
    if(b == 0){
      return 1;
  }
  return potenciaRecursiva(a,b-1)*a;
  }

  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    System.out.println(potenciaRecursiva(a,b));

  }
}
