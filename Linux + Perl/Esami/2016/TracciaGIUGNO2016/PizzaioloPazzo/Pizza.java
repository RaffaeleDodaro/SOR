package PizzaioloPazzo;

import java.util.Random;

public class Pizza {

    final public static String alphabet = ";:#@-!£$?*Oo";
    final public static Random r = new Random();
    public static char generaCharRandom()
    {
    	return alphabet.charAt(r.nextInt(alphabet.length()));
    }
	
}
