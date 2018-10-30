import com.jogamp.opengl.GLAutoDrawable;
import com.jogamp.opengl.util.gl2.GLUT;

/**
 @author veronika K. on 27.09.18 */
public class Teapot
	extends CustomShape {

	private double scale;
	private final GLUT glut = new GLUT();

	public Teapot(final GLAutoDrawable drawable, final double scale) {
		super(drawable);
		this.scale = scale;
	}

	@Override
	public void drawSolid() {
		glut.glutSolidTeapot(scale);
	}

	@Override
	public void drawWire() {
		glut.glutWireTeapot(scale);
	}

	public void scale(final double scale) {
		this.scale = scale;
	}
}
