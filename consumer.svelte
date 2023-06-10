<script lang="ts">
  import { browser } from "$app/environment";
  import { onDestroy, onMount } from "svelte";
  let data = {};
  let ws: any;

  if (browser) {
    ws = new WebSocket("ws://127.0.0.1:8000/ws/posts/");
  }
  onMount(() => {
    ws.addEventListener("message", (e: any) => {
      data = structuredClone(e.data);
    });
  });
  function OnClick() {
    ws.send(
      JSON.stringify({
        action: "create",
        request_id: new Date().getTime(),
        data: {
          title: "new user 4",
          description: "testpassword123",
        },
      })
    );
  }
  onDestroy(() => {
    ws?.close();
  });
</script>

<button on:click={OnClick}> Create New Post </button>
<a href="/some">Some</a>
<pre>
    {JSON.stringify(data, null, 2)}
</pre>
