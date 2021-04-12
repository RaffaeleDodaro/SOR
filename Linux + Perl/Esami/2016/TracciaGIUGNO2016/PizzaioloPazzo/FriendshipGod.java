package PizzaioloPazzo;

import java.util.Random;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class FriendshipGod extends Thread
{
	BlockingQueue<String> tavoli = new ArrayBlockingQueue(20);
	//
	// Chiama questo metodo quando vuoi gestire una nuova comitiva in arrivo
	//
	public String getTavolo() throws InterruptedException
	{
		return tavoli.take();
	}
	public void run()
	{
		try {

			Random r = new Random();
			while(true)
			{
				    // ogni comitiva è composta da massimo 20 persone e viene generata già con
				    // degli ordini di pizze scelte a caso per ciascun commensale
				    int n = r.nextInt(20)+1;
				    String tavolo = "";
				    for (int i = 0; i < n; i++)
				    	tavolo = tavolo + "[" + Pizza.generaCharRandom() + "]";
					sleep(10000);
					tavoli.put(tavolo);
			}
				} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} 

		}
}
