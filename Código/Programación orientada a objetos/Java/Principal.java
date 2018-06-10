/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package prueba;

import java.util.Scanner;

/**
 *
 * @author curso
 */
public class Principal {
    public static void main(String[] args){
        Prueba oper = new Prueba();
        int opcion = 0;
        do{
            System.out.println("**** Menu****");
            System.out.println("1- Sumar");
            System.out.println("2- Restar");
            System.out.println("3- Multiplicar");
            System.out.println("4- Dividir");
            System.out.println("Ingrese la opcion que desea ejecutar:");
            Scanner entrada = new Scanner(System.in);
            
            opcion =entrada.nextInt();
            if(opcion != 5 ){
            
                System.out.println("Ingrese el valor 1: ");
                int valor1 = entrada.nextInt();
                System.out.println("Ingrese el valor 2: ");
                int valor2 = entrada.nextInt();
                double resultado = 0;
                switch(opcion){
                    case 1: resultado = oper.suma(valor1, valor2);
                       break;
                    case 2: resultado = oper.resta(valor1, valor2);
                       break;
                    case 3: resultado = oper.multiplicacion(valor1, valor2);
                        break;
                    case 4: resultado = oper.division(valor1, valor2);
                        break;
                    default:
                        System.out.println("No se realizo ninguna operacion.");
        
        }
        System.out.println("El resultado es: " + resultado);
    }
}while(opcion >= 1 && opcion < 5);
    
}
}
