//
// Rinominare questo package con nomeCognomeMatricola
//
package traghettoLuglio2016;


public class Traghetto {

	SorgenteVetture sorgente = new SorgenteVetture();
	
	//
	// ...
	//

	void CaricaTraghetto()
	{
		
		sorgente.start();
		
		Parcheggiatore[] omino = new Parcheggiatore[4];

		for(int i = 0; i < 4; i++)
		{
			omino[i] = new Parcheggiatore(this);
			omino[i].start();
		}
		//
		//  Il resto è a carico tuo
		//
		
		// .... 
		
		
		
		// Questo metodo non può terminare prima che il traghetto non sia pieno di vetture.
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
