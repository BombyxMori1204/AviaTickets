const plane = document.querySelector(".scroll-plane");

if (plane) {
	let frameRequested = false;
	const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

	const updatePlanePosition = () => {
		const scrollableDistance = document.documentElement.scrollHeight - window.innerHeight;
		const progress = !prefersReducedMotion.matches && scrollableDistance > 0
			? window.scrollY / scrollableDistance
			: 0;
		const planeSize = plane.getBoundingClientRect().width;
		const horizontalDistance = Math.max(0, window.innerWidth - planeSize - 48);
		const verticalDistance = window.innerHeight * 0.72;

		plane.style.setProperty("--plane-x", `${horizontalDistance * progress}px`);
		plane.style.setProperty("--plane-y", `${-verticalDistance * progress}px`);
		frameRequested = false;
	};

	const requestPlanePositionUpdate = () => {
		if (!frameRequested) {
			window.requestAnimationFrame(updatePlanePosition);
			frameRequested = true;
		}
	};

	window.addEventListener("scroll", requestPlanePositionUpdate, { passive: true });
	window.addEventListener("resize", requestPlanePositionUpdate);
	updatePlanePosition();
}
