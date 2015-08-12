/* Wall.java */

public class Wall {
	private int i;
	private int j;
	private String type;

	public Wall(int i, int j, String type) {
		this.i = i;
		this.j = j;
		this.type = type;
	}

	public int getX() {
		return i;
	}

	public int getY() {
		return j;
	}

	public String getType() {
		return type;
	}

	public String toString() {
		String s = "This wall is a " + type + " wall on (" + i + ", " + j + ").";
		return s;
	}

	public static void main(String[] args) {
		Wall w = new Wall(1,3, "horiz");
		System.out.println(w);
	}
}