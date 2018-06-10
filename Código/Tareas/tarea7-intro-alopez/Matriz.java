
public class Matriz {
        public static void main (String args[]){
            int matriz1[][]={{1,2,3},{4,5,6}};
            int matriz2[][]={{7,8},{9,10},{11,12}};
            int row1=matriz1.length;
            int row2=matriz2.length;
            int col1=matriz1[0].length;
            int col2=matriz2[0].length;
            int matriz[][]=new int[row1][col2];



            for (int x=0; x < matriz.length; x++) {
                for (int y = 0; y < matriz[x].length; y++) {
                    for(int t=0; t < col1; t++) {
                        matriz[x][y] += matriz1[x][t] * matriz2[t][y];
                    }
            }

        }
        


            String valores="";

            for(int fila1=0;fila1<matriz.length;fila1++)
            {
                for(int columna1=0;columna1<matriz[0].length;columna1++)
                {
                    valores+=" "+matriz[fila1][columna1];
                }
                valores+="\n";
            }
            System.out.println(valores);
        }

    }



