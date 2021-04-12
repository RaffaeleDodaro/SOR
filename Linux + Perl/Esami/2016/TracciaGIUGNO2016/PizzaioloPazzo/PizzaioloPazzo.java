package PizzaioloPazzo;

import java.util.Random;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class PizzaioloPazzo extends Thread {


	
	BlockingQueue<String> pizzePronte = new ArrayBlockingQueue<String>(10);

	//
	// Chiama questo metodo quando vuoi prendere una pizza cucinata dal pizzaiolo pazzo
	//
	public String getPizza() throws InterruptedException
	{
		return pizzePronte.take();
	}

	public void run()
	{
		try {

		    Random r = new Random();

			while(true)
			{
				sleep(1000); // Genera una pizza al secondo.
				String pizza = "(" + Pizza.generaCharRandom() + ")";
				pizzePronte.put(pizza);
				
			}
		} 
		catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		}
}
