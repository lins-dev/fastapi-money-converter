# fastapi-money-converter

This is a simple FastAPI project designed to convert an amount in a given currency to a list of other selected currencies. The project uses FastAPI to create API endpoints and managed with [uv](https://github.com/astral-sh/uv)

<h2>✨Features</h2>
<div>
    <h4>🌍 Currency Conversion:</h4> Accepts a currency name (e.g., "USD") and amount to convert.
</div>
<div>
    <h4>📊 Multiple Currencies:</h4> Converts the amount to a user-selected list of other currencies.
</div>
<div>
    <h4>⚡ Real-time Rates:</h4> Fetches up-to-date conversion rates from an external API.
</div>
<div>
    <h4>🔧 Scalable Structure:</h4> Modular and extendable project layout with FastAPI.
</div>
<h2>📋 Requirements</h2>
<div>
    <table>
        <thead>
            <tr>
                <th>Package</th>
                <th>Version</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Python</td>
                <td>3.13</td>
            </tr>
            <tr>
                <td>aiohttp</td>
                <td>3.10.10</td>
            </tr>
            <tr>
                <td>fastapi[standard]</td>
                <td>0.115.4</td>
            </tr>
            <tr>
                <td>pydantic-settings</td>
                <td>2.6.1</td>
            </tr>
            <tr>
                <td>python-dotenv</td>
                <td>1.0.1</td>
            </tr>
            <tr>
                <td>requests</td>
                <td>2.32.3</td>
            </tr>
        </tbody>
    </table>
</div>

## License

MIT

<h2>🌐 Usage</h2>
Run the Application
Use uv to start the FastAPI server:
<div>
<code>
uv run fastapi dev --port=8080
</code>
</div>