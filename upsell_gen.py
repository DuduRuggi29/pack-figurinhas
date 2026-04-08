with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract from line 0 to line 281 (0-indexed 0 to 280) -> this captures <head> completely and <body ...> and <div class="elementor ...">
head_part = "".join(lines[:281])

# Extract the very bottom scripts and closing tags (lines 1819 to end)
footer_part = "".join(lines[1819:])

body_upsell = """
<section class="elementor-section elementor-top-section elementor-element elementor-section-boxed elementor-section-height-default" style="background-color: #111; color: #fff; min-height: 80vh; display: flex; align-items: center; justify-content: center; padding: 60px 20px;">
<div class="elementor-container">
   <div style="max-width: 800px; margin: 0 auto; text-align: center; font-family: 'Inter', sans-serif;">
       
       <div style="background-color: #cc0000; color: white; padding: 10px 20px; border-radius: 8px; display: inline-block; margin-bottom: 25px; font-weight: bold; font-size: 18px; text-transform: uppercase; animation: pulse 2s infinite;">
           Atenção: Não feche ou atualize essa página!
       </div>

       <h2 style="font-size: clamp(28px, 5vw, 42px); font-weight: 800; margin-bottom: 20px; line-height: 1.2;">
           ESPERE! LEVE <span style="color: #ffd700;">TODOS OS BÔNUS</span> ALÉM DO PACOTE DE FIGURINHAS POR:
       </h2>
       
       <h1 style="font-size: clamp(40px, 8vw, 60px); color: #ffd700; font-weight: 900; margin-bottom: 30px;">
           R$ 10,90
       </h1>
       
       <p style="font-size: 18px; line-height: 1.6; margin-bottom: 40px; color: #ddd;">
        Nós iremos te oferecer um <strong>desconto exclusivo</strong>. Normalmente para levar a oferta VIP (Acesso Vitalício +500 Figurinhas Premium, +1.000 Minimalistas, Sombras, Molduras e Cursos de Stories/Ads) você pagaria <strong>R$ 15,99</strong>. Mas como você já está levando a oferta básica, vamos deixar tudo isso por <strong>apenas R$ 10,90</strong>.
       </p>
       
       <div style="margin-bottom: 40px;">
           <a href="#" style="background-color: #28a745; color: #fff; padding: 20px 40px; font-size: clamp(16px, 4vw, 24px); font-weight: 800; border-radius: 8px; text-decoration: none; display: inline-block; box-shadow: 0 4px 15px rgba(40,167,69,0.5); text-transform: uppercase; width: 100%; max-width: 500px;">
               SIM, QUERO ADICIONAR TUDO ISSO!
           </a>
           <p style="margin-top: 10px; font-size: 12px; color: #aaa;">* Preciso do link de checkout de 10,90 para adicionar neste botão.</p>
       </div>
       
       <div style="margin-top: 40px;">
           <a href="https://pay.cakto.com.br/77cgkfi" style="color: #888; font-size: 15px; text-decoration: underline;">
               Não, quero a oferta básica mesmo por R$ 5,99 e abrir mão dos bônus extras.
           </a>
       </div>
   </div>
</div>
</section>
"""

with open('upsell.html', 'w', encoding='utf-8') as f:
    f.write(head_part + body_upsell + "</div>" + footer_part)
