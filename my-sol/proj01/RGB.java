public class RGB {
	public short red;
	public short green;
	public short blue;

	public RGB() {
		red = 0;
		green = 0;
		blue = 0;
	}

	public RGB(short red, short green, short blue) {
		this.red = red;
		this.green = green;
		this.blue = blue;
	}

	public short getColor(String color) {
		if (color.equals("red")) {
			return red;
		} else if (color.equals("green")) {
			return green;
		} else {
			return blue;
		}
	}

	public short getRed() {
		return red;
	}

	public short getGreen() {
		return green;
	}

	public short getBlue() {
		return blue;
	}

	public String toString() {
		return "(" + getRed() + "," + getGreen() + "," +getBlue() + ")";
	}

	public static void main(String[] args) {
		RGB rgb = new RGB();
		System.out.println(rgb.red + " " + rgb.green + " " + rgb.blue);

		short red, green, blue; 
		red = 100;
		green = 200;
		blue = 240;
		RGB rgb2 = new RGB(red, green, blue);
		System.out.println(rgb2.red + " " + rgb2.green + " " + rgb2.blue);

		RGB[] rgb3 = new RGB[2];
		rgb3[0] = rgb;
		rgb3[1] = rgb2;

		for (RGB color : rgb3) {
			System.out.println(color.red + " " + color.green + " " + color.blue);
		}

		System.out.println("rgb2's green is " + rgb2.getColor("green"));

		try {
			System.out.println(rgb3[-1].red);
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println(rgb3[0].red);
		}

		System.out.println(rgb2);
		
	}
}