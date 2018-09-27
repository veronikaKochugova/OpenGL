import com.jogamp.opengl.GL;
import com.jogamp.opengl.GLAutoDrawable;
import com.jogamp.opengl.GLCapabilities;
import com.jogamp.opengl.GLEventListener;
import com.jogamp.opengl.GLProfile;
import com.jogamp.opengl.awt.GLCanvas;

import java.awt.*;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Arrays;

/**
 @author veronika K. on 26.09.18 */
public class Task1
	implements GLEventListener {

	private static Frame mainFrame;
	private static double DX = 0.0;
	private static double DY = 0.0;

	public static void main(String[] args) {
		final GLProfile glProfile = GLProfile.get(GLProfile.GL2);
		final GLCapabilities glCapabilities = new GLCapabilities(glProfile);
		final GLCanvas canvas = new GLCanvas(glCapabilities);
		final Task1 task1 = new Task1();
		canvas.addGLEventListener(task1);
		canvas.setSize(400, 400);
		canvas.addKeyListener(new KeyListener() {
			@Override
			public void keyTyped(final KeyEvent keyEvent) {
			}

			@Override
			public void keyPressed(final KeyEvent keyEvent) {
				DX += 100.0;
				DY += - 70.0;
				System.out.println("KEY " + keyEvent.getKeyChar());
				System.out.println(DX);
				canvas.display();
			}

			@Override
			public void keyReleased(final KeyEvent keyEvent) {
			}
		});
		mainFrame = FrameUtil.frame("Task1", Arrays.asList(canvas));
	}

	@Override
	public void init(final GLAutoDrawable drawable) {
	}

	@Override
	public void dispose(final GLAutoDrawable drawable) {
	}

	@Override
	public void display(final GLAutoDrawable drawable) {
		subTask1(drawable);
		subTask2(drawable);
	}

	public void subTask1(final GLAutoDrawable drawable) {
		drawable.getGL().getGL2().glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT);
		final CustomShape teapot = new Teapot(drawable, 0.25);
		final CustomShape sphere = new Sphere(drawable, 0.25);
		teapot.moveOnX(DX / mainFrame.getWidth());
		System.out.println(DX);
		teapot.drawWire();
		teapot.moveOnX(- DX / mainFrame.getWidth());
		sphere.moveOnY(DY / mainFrame.getHeight());
		sphere.drawWire();
	}

	public void subTask2(final GLAutoDrawable drawable) {
		drawable.getGL().getGL2().glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT);
		final CustomShape cylinder = new Cylinder(drawable, 0.25, 0.25);
		cylinder.rotate(60, 100, 0, 0);
		cylinder.drawWire();
		final CustomShape tetrahedron = new Tetrahedron(drawable);
		tetrahedron.moveOnX(DX * 3 / mainFrame.getWidth());
		tetrahedron.rotate(45, 40, 40, 0);
		tetrahedron.scale(0.6, 0.6, 0.6);
		tetrahedron.drawWire();
	}

	@Override
	public void reshape(final GLAutoDrawable drawable, final int x, final int y, final int width, final int height) {
	}
}
