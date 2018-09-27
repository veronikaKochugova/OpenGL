import com.jogamp.opengl.GLAutoDrawable;
import com.jogamp.opengl.util.gl2.GLUT;

/**
 @author veronika K. on 27.09.18 */
public class Cylinder
	extends CustomShape {

	private final GLUT glut = new GLUT();
	private int stacks = 50;
	private double radius;
	private double height;
	private int slices = 50;

	public Cylinder(final GLAutoDrawable drawable, final double radius, final double height) {
		super(drawable);
		this.radius = radius;
		this.height = height;
	}

	@Override
	void drawSolid() {
		glut.glutSolidCylinder(radius, height, slices, stacks);
	}

	@Override
	void drawWire() {
		glut.glutWireCylinder(radius, height, slices, stacks);
	}
}
