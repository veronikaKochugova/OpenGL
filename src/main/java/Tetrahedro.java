import com.jogamp.opengl.GLAutoDrawable;
import com.jogamp.opengl.util.gl2.GLUT;

/**
 @author veronika K. on 27.09.18 */
public class Tetrahedro extends CustomShape {

	private final GLUT glut = new GLUT();
//	private int stacks = 50;
//	private double radius;
//	private double height;
//	private int slices = 50;

	public Tetrahedro(final GLAutoDrawable drawable) {
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
