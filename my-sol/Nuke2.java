/* Nuke2.java*/

import java.io.*;

/**  A class that provides a main function to read a line and print
 *   them , with its second character omited.
 */

class Nuke2 {

	public static void main(String[] args) throws Exception {
		BufferedReader keyboard 
			= new BufferedReader(new InputStreamReader(System.in));

		String line = keyboard.readLine();
		String lineOmited = line.charAt(0) + line.substring(2);
		System.out.println(lineOmited);
	}
}