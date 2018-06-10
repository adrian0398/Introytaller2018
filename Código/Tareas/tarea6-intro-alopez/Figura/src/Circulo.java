import java.lang.Math;
public class Circulo extends Figura {
    protected int r;

    public Circulo(int x, int y, int r)
    {
        super(x, y);
        this.r=r;
    }

    public void setRadio(int r)
    {
        this.r=r;
    }
    public int getRadio()
    {
        return r;
    }

    public double calcularArea()
    {
        return Math.PI*(r*r);
    }

}
