const BASE_URL = 'https://api.jikan.moe/v4'

function makeRequest(endpoint, params) {
    return fetch(`${BASE_URL}/${endpoint}/${params}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(response)
            }
            return response.json()
        })
        .then(json => {
            return json.data;
        });
}

function initScrollBehavior(className) {
    const containers = document.querySelectorAll(`.${className}`);

    containers.forEach((container) => {
        const animeContainer = container.querySelector('.anime-scroll')
        const scrollLeftButton = container.querySelector('#scroll-left');
        const scrollRightButton = container.querySelector('#scroll-right');
        const cardWidth = animeContainer.children[0].offsetWidth;

        if (animeContainer.scrollLeft === 0) {
            scrollLeftButton.classList.add('opacity-50', 'cursor-not-allowed');
        } else {
            scrollLeftButton.classList.remove('opacity-50', 'cursor-not-allowed');
        }
        animeContainer.addEventListener('scroll', () => {
            if (animeContainer.scrollLeft === 0) {
                scrollLeftButton.classList.add('opacity-50', 'cursor-not-allowed');
            } else {
                scrollLeftButton.classList.remove('opacity-50', 'cursor-not-allowed');
            }
        });
        scrollLeftButton.addEventListener('click', () => {
            console.log(screen.width);
            animeContainer.scrollLeft -= cardWidth * screen.width <= 640 ? 2 : 5;
        });

        scrollRightButton.addEventListener('click', () => {
            console.log(screen.width <= 640 ? 2 : 5)
            animeContainer.scrollLeft += cardWidth * 2;
        });
    });
}