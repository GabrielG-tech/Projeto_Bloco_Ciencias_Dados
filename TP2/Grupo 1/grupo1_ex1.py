import aiohttp
import asyncio

async def fetch_data(url):
    # cria sessão HTTP assíncrona
    async with aiohttp.ClientSession() as session:
        # requisição GET à URL
        async with session.get(url) as response:
            # retorno dados em JSON
            return await response.json()

async def main():
    # define a URL da API pública
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # chama a função fetch_data para buscar os dados da API
    data = await fetch_data(url)
    
    print(data)

# inicia o loop de eventos assíncronos e executa a função main()
asyncio.run(main())
