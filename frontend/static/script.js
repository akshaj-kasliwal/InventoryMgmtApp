// frontend/static/script.js

document.getElementById("balance-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    const itemId = document.getElementById("item-id").value;

    // Fetch balance data from the API
    const response = await fetch(`/inventory/${itemId}/balance`);
    const data = await response.json();

    // Check for an error response
    if (response.status !== 200) {
        document.getElementById("balance-details").innerHTML = `<p>Error: ${data.detail}</p>`;
        return;
    }

    // Display balance details
    const resultHtml = `<div>
                          <p>Item ID: ${data.item_id}</p>
                          <p>Balance: ${data.balance}</p>
                        </div>`;
   document.getElementById("balance-result").innerHTML = resultHtml;  // Insert HTML content

});
