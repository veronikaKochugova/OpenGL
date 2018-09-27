import com.jogamp.opengl.GLAutoDrawable;
import com.jogamp.opengl.util.gl2.GLUT;

/**
 @author veronika K. on 27.09.18 */
public class Tetrahedron
	extends CustomShape {

	private final GLUT glut = new GLUT();

	public Tetrahedron(final GLAutoDrawable drawable) {
		super(drawable);
	}

	@Override
	void drawSolid() {
		glut.glutSolidTetrahedron();
	}

	@Override
	void drawWire() {
		glut.glutWireTetrahedron();
	}
}
