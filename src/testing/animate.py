import pygifsicle
import imageio
import time

from src_fractal import generateFractal

def main():
    print("Generating gif...")

    start = time.time()
    frames = []

    for i in range(1, 201):
        i /= 200

        frames.append(generateFractal(1, 1, i, [44, 84, 165], [28, 166, 150], "sphericalVariation", 100000))

    frames = frames + list(reversed(frames))

    with open("out.gif", "wb") as out_gif:
        imageio.mimwrite(out_gif, frames, format="gif", fps=40)

    pygifsicle.optimize("out.gif")

    print(f"Finished generation in {round(time.time() - start)} seconds.")

if __name__ == "__main__":
    main()
