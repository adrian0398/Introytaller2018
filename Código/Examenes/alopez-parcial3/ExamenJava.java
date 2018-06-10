import java.util.Scanner;
public class ExamenJava {
    public static void main(String Args[]){
        Scanner sc=new Scanner(System.in);
        System.out.println("Ingrese valor");
        int valor=sc.nextInt();
        System.out.println("Digitos : "+ contar(valor));

        System.out.print("Ingrese longitud");
        int longitud=sc.nextInt();
        int[] lista=new int[longitud];
        for(int z=0;z<longitud;z++){
            System.out.println("Ingrese valor");
            int num=sc.nextInt();
            lista[z]=num;
        }
        lista=ordenar(lista,longitud);
        for(int m=0;m<longitud;m++){
            System.out.println(lista[m]);
        }


    }

    public static int contar(int valor){
        int longitud=0;
        while(valor>1){
            longitud+=1;
            valor=valor/10;


        }
        return longitud;


    }

    public static int[] ordenar(int[]lista,int longitud){
        int menor=lista[0];
        int[] lista2=new int[longitud];
        int pos=0;
        for(int i=0;i<longitud;i++){
            int [] lista3=new int [longitud-i-1];
            for(int t=0;t<longitud;t++){
                if (menor>lista[t]){
                        menor=lista[t];
                        pos =t;
                }



            }
            int x=0;
            for(int s=0;s<longitud-s-1;s++){
                if (s!=pos){
                    lista3[s]=lista[x];
                    x++;
                }
                if (s==pos){
                    lista3[s]=lista[x+1];
                    x=x+2;
                }
            }
            lista=lista3;
            lista2[i]=menor;
            menor=lista[0];


        }

        return lista2;



    }



}
