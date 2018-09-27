import com.jogamp.opengl.GL;
import com.jogamp.opengl.GL2;
import com.jogamp.opengl.GL2ES3;
import com.jogamp.opengl.GLAutoDrawable;
import com.jogamp.opengl.GLCapabilities;
import com.jogamp.opengl.GLEventListener;
import com.jogamp.opengl.GLProfile;
import com.jogamp.opengl.awt.GLCanvas;
import com.jogamp.opengl.glu.GLU;
import com.jogamp.opengl.util.gl2.GLUT;

import java.awt.*;
import java.util.Arrays;
import java.util.concurrent.TimeUnit;

/**
 @author veronika K. on 26.09.18 */
public class Task1
	implements GLEventListener {

	public static void main(String[] args) {
		final GLProfile glProfile = GLProfile.get(GLProfile.GL2);
		final GLCapabilities glCapabilities = new GLCapabilities(glProfile);
		final GLCanvas canvas = new GLCanvas(glCapabilities);
		final Task1 task1 = new Task1();
		canvas.addGLEventListener(task1);
		canvas.setSize(400, 400);
		final Frame frame = FrameUtil.frame("Task1", Arrays.asList(canvas));
	}

	@Override
	public void init(final GLAutoDrawable drawable) {
	}

	@Override
	public void dispose(final GLAutoDrawable drawable) {
	}

	@Override
	public void display(final GLAutoDrawable drawable) {
		final CustomShape teapot = new Teapot(drawable, 0.25);
		final CustomShape sphere = new Sphere(drawable, 0.25);
		teapot.moveOnX(0.5);
		teapot.drawWire();
		sphere.moveOnX(-1);
		sphere.drawWire();
		//
		drawable.getGL().getGL2().glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT);
		final CustomShape cylinder = new Cylinder(drawable,0.25,0.25);
		cylinder.drawWire();
		final CustomShape tetrahedron = new Tetrahedro(drawable);
		tetrahedron.moveOnX(-0.5);
		tetrahedron.drawWire();
	}

	private void drawTeapot(final GLAutoDrawable drawable) {
		final GL2 gl = drawable.getGL().getGL2();
		gl.glColor3b((byte) 0, (byte) 1, (byte) 0);
		gl.glBegin(GL2ES3.GL_QUADS);
		{
			gl.glVertex2d(-2,1);
			gl.glVertex2d(2,2.0);
		}
		gl.glEnd();
	}

	@Override
	public void reshape(final GLAutoDrawable drawable, final int x, final int y, final int width, final int height) {
	}
}
