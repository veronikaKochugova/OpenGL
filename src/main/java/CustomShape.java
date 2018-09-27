import com.jogamp.opengl.GL;
import com.jogamp.opengl.GL2;
import com.jogamp.opengl.GLAutoDrawable;

/**
 @author veronika K. on 27.09.18 */
abstract class CustomShape {

	protected GL2 gl;

	public CustomShape(final GLAutoDrawable drawable) {
		this.gl = drawable.getGL().getGL2();
		gl.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT);
		gl.glLoadIdentity();
	}

	abstract void drawSolid();

	abstract void drawWire();

	public void moveOnX(final double dx) {
		gl.glTranslated(dx, 0, 0);
	}
}
