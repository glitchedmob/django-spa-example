<template>
	<div class="container">
		<template v-if="posts.length == 0">
			<h1 class="no-posts">No posts</h1>
		</template>
		<template v-else>
			<b-card
				v-for="(post, index) in posts"
				:key="index"
				:title="post.title"
				tag="article"
				class="mb-4">
			<p class="card-text">
				{{ post.body }}
			</p>
			<b-button :to="{ name: 'view-post', params: { id: post.id } }" variant="primary">View</b-button>
		</b-card>
		</template>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	data: () => ({
		posts: []
	}),
	created() {
		axios.get('api/posts/')
			.then(response => this.posts = response.data)
	}
}
</script>

<style lang="scss" scoped>
	.container {
		margin-top: 1rem;
	}

	.no-posts {
		text-align: center;
	}
</style>

