public class Figura {

    protected int x;
    protected int y;

    public Figura(int x, int y)
    {
        this.x=x;
        this.y=y;
    }

    public void setX(int x)
    {  if(x>=0 ^ x<=1023){
        this.x=x;}
    else{
        System.out.println("El valor de x debe ser mayor o igual a 0 y menor a 1024.");}
    }
    public int getX()
    {
        return x;
    }
    public void setY(int y)
    {  if(y>=0 ^ y<=768){
        this.y=y;}
        else{
        System.out.println("El valor de y debe ser mayor o igual a 0 y menor a 768.");}
    }
    public int getY()
    {
        return y;
    }



}
