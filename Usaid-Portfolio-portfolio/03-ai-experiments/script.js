const topic = document.getElementById("topic");
const styleChoice = document.getElementById("style");
const result = document.getElementById("result");

document.getElementById("build").addEventListener("click", function () {
    const idea = topic.value.trim();

    if (idea === "") {
        result.textContent = "Please enter something you want to create first.";
        return;
    }

    result.textContent =
        "Act as a helpful assistant. Help me create " + idea +
        ". Use a " + styleChoice.value.toLowerCase() +
        " approach. Give me clear steps, useful examples and a well-organized result.";
});

document.getElementById("copy").addEventListener("click", async function () {
    const text = result.textContent;

    try {
        await navigator.clipboard.writeText(text);
        this.textContent = "Copied!";
    } catch (error) {
        this.textContent = "Select and copy the prompt";
    }
});