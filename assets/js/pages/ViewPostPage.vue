<template>
	<div class="container">
		<b-card
			:title="post.title"
			tag="article"
			class="mb-4">
			<p class="card-text">
				{{ post.body }}
			</p>
		</b-card>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	data: () => ({
		post: {}
	}),
	created() {
		const postId = this.$route.params.id;

		axios.get(`api/posts/${postId}/`)
			.then(response => this.post = response.data)
	}
}
</script>

<style lang="scss" scoped>
	.container {
		margin-top: 1rem;
	}
</style>
