* {
  box-sizing: border-box;
}

:root {
  --bg: #0b1020;
  --panel: rgba(255, 255, 255, 0.06);
  --panel-strong: rgba(255, 255, 255, 0.1);
  --text: #eef3ff;
  --muted: #b7c2d9;
  --accent: #6ee7b7;
  --accent-2: #60a5fa;
  --shadow: rgba(0,0,0,0.34);
}

body {
  margin: 0;
  background: linear-gradient(135deg, #0b1020, #111827 50%, #0f172a);
  color: var(--text);
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}

img {
  max-width: 100%;
  display: block;
}

.topbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 40px;
  border-bottom: 1px solid rgba(255,255,255,0.08);
  background: rgba(11, 16, 32, 0.72);
  backdrop-filter: blur(18px);
  position: sticky;
  top: 0;
  z-index: 5;
}

.brand {
  font-size: 1.5rem;
  font-weight: 800;
  letter-spacing: 0.08em;
}

.nav {
  display: flex;
  gap: 18px;
  align-items: center;
}

.nav a {
  color: var(--text);
  text-decoration: none;
  opacity: 0.8;
}

.page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 32px 20px 60px;
}

.hero {
  padding: 32px 0 12px;
}

.eyebrow {
  color: var(--accent);
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-weight: 700;
  font-size: 0.72rem;
}

.hero h1 {
  font-size: clamp(2.2rem, 4vw, 4rem);
  margin: 8px 0 12px;
}

.lead {
  color: var(--muted);
  max-width: 700px;
}

.filters {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin: 18px 0 28px;
}

.filter-pill {
  background: rgba(255,255,255,0.06);
  color: var(--text);
  border: 1px solid rgba(255,255,255,0.08);
  padding: 9px 16px;
  border-radius: 999px;
  cursor: pointer;
}

.filter-pill.active {
  background: linear-gradient(135deg, var(--accent), var(--accent-2));
  color: #08111f;
  font-weight: 700;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 22px;
}

.card {
  border-radius: 18px;
  overflow: hidden;
  background: var(--panel);
  border: 1px solid rgba(255,255,255,0.08);
  box-shadow: 0 16px 32px var(--shadow);
}

.card img {
  width: 100%;
  height: 320px;
  object-fit: cover;
}

.content {
  padding: 18px 16px 20px;
}

.meta-row {
  display: flex;
  justify-content: space-between;
  color: var(--muted);
  font-size: 0.8rem;
}

.card h3 {
  margin: 12px 0 8px;
  font-size: 1.1rem;
}

.card p {
  margin: 0 0 12px;
  color: var(--muted);
  line-height: 1.5;
}

.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}

.button {
  display: inline-block;
  text-decoration: none;
  background: rgba(255,255,255,0.1);
  color: var(--text);
  border: 1px solid rgba(255,255,255,0.12);
  border-radius: 11px;
  padding: 10px 12px;
  font-weight: 600;
}

.button.primary {
  background: linear-gradient(135deg, var(--accent), var(--accent-2));
  color: #08111f;
}

.auth-body {
  min-height: 100vh;
  display: grid;
  place-items: center;
}

.auth-box {
  width: min(440px, 90vw);
  background: var(--panel);
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 18px;
  padding: 24px;
  box-shadow: 0 18px 38px var(--shadow);
}

.auth-box h2 {
  margin-top: 0;
}

.auth-box form,
.settings-form,
.admin-form {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

input, textarea, button {
  width: 100%;
  border-radius: 10px;
  border: 1px solid rgba(255,255,255,0.08);
  padding: 12px 14px;
  background: rgba(255,255,255,0.04);
  color: var(--text);
}

button {
  background: linear-gradient(135deg, var(--accent), var(--accent-2));
  color: #08111f;
  font-weight: 700;
  border: none;
  cursor: pointer;
}

.error {
  color: #ff9aa8;
}

.admin-page,
.settings-page {
  padding-top: 40px;
}

.admin-actions {
  margin: 16px 0 24px;
}

.form-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 12px;
}

.admin-form textarea {
  min-height: 100px;
}

.admin-list {
  margin-top: 28px;
  display: grid;
  gap: 12px;
}

.mini-card {
  display: flex;
  justify-content: space-between;
  padding: 12px 14px;
  border-radius: 12px;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.08);
}

.detail-page {
  padding-top: 32px;
}

.detail-header {
  display: grid;
  grid-template-columns: 320px 1fr;
  gap: 22px;
  align-items: center;
}

.detail-header img {
  width: 100%;
  border-radius: 18px;
  box-shadow: 0 18px 40px rgba(0,0,0,0.4);
}

.detail-copy {
  color: var(--text);
}

.detail-copy h1 {
  margin: 8px 0 12px;
}

.detail-copy p {
  color: var(--muted);
  line-height: 1.7;
}

.detail-actions {
  display: flex;
  gap: 12px;
  margin-top: 16px;
  flex-wrap: wrap;
}

@media (max-width: 760px) {
  .topbar {
    padding: 16px 18px;
    flex-wrap: wrap;
    gap: 10px;
  }

  .detail-header {
    grid-template-columns: 1fr;
  }
}
