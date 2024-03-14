import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider


def interpolate_lines(u, v, t):
    line1 = u + t * v
    line2 = 2 * u - t * v
    return line1 + t * (line2 - line1)


def update_plot(frame, ax_3d, ax_proj, u, v, t_slider, show_projections):
    ax_3d.clear()
    ax_proj.clear()

    t = frame / 100.0
    u, v = np.meshgrid(u, v)
    x = u
    y = v
    z = interpolate_lines(u, v, t)

    ax_3d.plot_surface(x, y, z, cmap='viridis', alpha=0.7, rstride=5, cstride=5, edgecolor='k', linewidth=2.0)
    ax_3d.scatter(u, v, z, color='red', s=20, label='Interpolation Points')

    if show_projections:
        ax_3d.contour(u, v, z, zdir='z', offset=0, colors='purple', linestyles='dashed', linewidths=2.0)
        ax_3d.contour(u, v, x, zdir='x', offset=0, colors='yellow', linestyles='dashed', linewidths=2.0)
        ax_3d.contour(u, v, y, zdir='y', offset=0, colors='green', linestyles='dashed', linewidths=2.0)

    ax_3d.set_xlabel('X')
    ax_3d.set_ylabel('Y')
    ax_3d.set_zlabel('Z')
    ax_3d.set_title(f'Interpolating Lines Q(u, v) for t={t:.2f}')
    ax_3d.legend()

    ax_proj.plot_surface(x, y, z, cmap='viridis', alpha=0.7, rstride=5, cstride=5, edgecolor='k', linewidth=2.0)

    if show_projections:
        # Make the filled projections half transparent
        ax_proj.contourf(u, v, z, zdir='z', offset=0, colors='purple', linestyles='dashed', alpha=0.5)
        ax_proj.contourf(u, v, x, zdir='x', offset=0, colors='yellow', linestyles='dashed', alpha=0.5)
        ax_proj.contourf(u, v, y, zdir='y', offset=0, colors='green', linestyles='dashed', alpha=0.5)

    ax_proj.set_xlabel('X')
    ax_proj.set_ylabel('Y')
    ax_proj.set_zlabel('Z')
    ax_proj.set_title('3D Surface and Projections')


def on_key(event):
    if event.key == 'enter':
        global show_projections
        show_projections = not show_projections
        plt.draw()


def update_animation(frame, ax_3d, ax_proj, u, v, t_slider, show_projections):
    update_plot(frame, ax_3d, ax_proj, u, v, t_slider, show_projections)


u = np.linspace(0, 1, 13)
v = np.linspace(0, 1, 13)

fig = plt.figure(figsize=(16, 8))
ax_3d = fig.add_subplot(121, projection='3d')
ax_proj = fig.add_subplot(122, projection='3d')

t_slider_ax = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
t_slider = Slider(t_slider_ax, 't', 0.0, 1.0, valinit=0.0)

fig.canvas.mpl_connect('key_press_event', on_key)

show_projections = True

animation = FuncAnimation(fig, update_animation, fargs=(ax_3d, ax_proj, u, v, t_slider, show_projections),
                          frames=100, interval=100)

plt.show()
