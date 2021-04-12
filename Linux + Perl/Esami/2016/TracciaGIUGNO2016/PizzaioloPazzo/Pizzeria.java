package PizzaioloPazzo;

import java.util.Random;
import java.util.Vector;

public class Pizzeria {


	PizzaioloPazzo joker;
	FriendshipGod bacco;
	//
	// Qui metterai i tavoli che arrivano. Se non ti piace il Vector, usa la struttura dati che preferisci.
	//
	Vector<String> tavoliASedere;
	
	Pizzeria()
	{
		joker = new PizzaioloPazzo();
		joker.start();
		bacco = new FriendshipGod();
		bacco.start();

		Cameriere[] sottoPagato = new Cameriere[4];

		for(int i = 0; i < 4; i++)
		{
			sottoPagato[i] = new Cameriere(this);
			sottoPagato[i].start();
		}
		
	}
	
	public static void main(String[] args)
	{
		Pizzeria thePizzeria = new Pizzeria();
	}
}
