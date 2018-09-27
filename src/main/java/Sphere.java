import com.jogamp.opengl.GLAutoDrawable;
import com.jogamp.opengl.util.gl2.GLUT;

/**
 @author veronika K. on 27.09.18 */
public class Sphere
	extends CustomShape {

	private final int slices = 70;
	private final int stacks = 70;
	private double radius;
	private final GLUT glut = new GLUT();

	public Sphere(final GLAutoDrawable drawable, final double radius) {
		super(drawable);
		this.radius = radius;
	}

	@Override
	public void drawSolid() {
		glut.glutSolidSphere(radius, slices, stacks);
	}

	@Override
	public void drawWire() {
		glut.glutWireSphere(radius, slices, stacks);
	}
}
