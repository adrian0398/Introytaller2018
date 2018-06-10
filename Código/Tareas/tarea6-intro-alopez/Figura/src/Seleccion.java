import java.util.Scanner;
public class Seleccion {
    Scanner in=new Scanner (System.in);

    Figura figura;
    Circulo circulo;
    Rectangulo rectangulo;
    int ancho;
    int alto;
    int r;
    int x;
    int y;

    public Seleccion(){
        System.out.println("Digite 1 para rectangulo, 2 para circulo");

        int num = in.nextInt();

        if (num==1){
            System.out.println("Ingrese x");
            int x = in.nextInt();
            System.out.println("Ingrese y");
            int y = in.nextInt();
            System.out.println("Ingrese ancho");
            int ancho = in.nextInt();
            System.out.println("Ingrese alto");
            int alto = in.nextInt();
            rectangulo=new Rectangulo(x,y,ancho,alto);
            System.out.println("El area es "+rectangulo.calcularArea());

        }

        if (num==2){
            System.out.println("Ingrese x");
            int x = in.nextInt();
            System.out.println("Ingrese y");
            int y = in.nextInt();
            System.out.println("Ingrese radio");
            int r = in.nextInt();
            circulo=new Circulo(x,y,r);
            System.out.println("El area es "+circulo.calcularArea());

        }




    }





    public static void main(String arg[])
    {
        Seleccion s=new Seleccion();
    }




}
