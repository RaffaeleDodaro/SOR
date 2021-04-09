//
// Rinominare questo package con nomeCognomeMatricola
//
package traghettoLuglio2016;


import java.util.Random;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

abstract class Vettura
{
	int size;
	void printSize()
	{
		System.out.println(size);
	}
}

class Automobile extends Vettura
{
	Automobile()
	{
		size = 2;
	}
}
class Autobus extends Vettura
{
	Autobus()
	{
		size = 4;
	}
}

public class SorgenteVetture extends Thread {


	
	BlockingQueue<Vettura> vetture = new ArrayBlockingQueue<Vettura>(10);

	//
	// Chiama questo metodo quando vuoi prendere una Vettura prodotta dalla SorgenteVettura
	//
	public Vettura getVettura() throws InterruptedException
	{
		return vetture.take();
	}

	public void run()
	{
		try {

		    Random r = new Random();

			while(true)
			{
				sleep(r.nextInt(100)); // Genera una vettura a intervalli casuali
				Vettura v = 
						r.nextInt(2) > 0 ? 
						new Automobile() : new Autobus();
				vetture.put(v);
				
			}
		} 
		catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		}
}

