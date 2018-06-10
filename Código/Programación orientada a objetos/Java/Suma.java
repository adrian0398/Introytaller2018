/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package suma;

/**
 *
 * @author curso
 */
import java.util.Scanner;
public class Suma {
    
    /**
     *
     * @return
     */
    public static  int[] llenarArray(){
    int longitudarray;
    int lista[];
    Scanner entrada = new Scanner(System.in);
    System.out.println("Ingrese la longitud del array");
    longitudarray =entrada.nextInt();
    
 
    lista = new int[longitudarray];
        
        
    int valor;
    System.out.println("Ingrese los valores de la lista");
    
    for(int i=0; i<longitudarray; i++){
        System.out.println("Ingrese valor");
        valor=entrada.nextInt();
        lista[i]=valor;
   
    }
    
    return lista;
    
        
       
}

    /**
     *
     * @param lista
     * @return
     */
    public static int sumaelementos(int[] lista){
        int suma1=0;
        
        for (int i=0; i<lista.length; i++) {
        
        suma1+=lista[i];    
        
        }
    
    
    return suma1;
    }
    
    
 


    
    
    public static void main(String[] args) {
     int lista[]=  llenarArray();
     int suma= sumaelementos(lista);
     System.out.println("Suma es " + suma);
      
    }
    
}


